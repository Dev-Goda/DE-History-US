"""
history_quiz.py
─────────────────────────────────────────────────────────────────
Run:   python history_quiz.py
Needs: Python 3 + tkinter (built-in)

Controls during quiz:
  1 / 2 / 3 / 4  → select answer
  Any key         → advance to next question (after answering)
─────────────────────────────────────────────────────────────────
Questions are loaded from .txt files inside the  questions/  folder
that lives next to this script.  Add more .txt files to get more
question sets — they appear automatically in the menu.

Missed questions are shuffled back into the remaining queue so you
keep seeing them until you get every question right at least once.

Question file format:
    # comment lines and blank lines are ignored

    CHAPTER: Some Chapter Name     ← optional; sets chapter tag
    Q: Question text here
    1: First choice
    2: Second choice
    3: Third choice
    4: Fourth choice
    ANSWER: 2                      ← number 1-4
    EXPLAIN: Why this answer is correct (optional — shown on wrong answer)
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import os
import glob


# ─────────────────────────────────────────────
#  QUESTION LOADER
# ─────────────────────────────────────────────
def load_questions_from_file(filepath):
    questions = []
    current_chapter = "General"
    q = None

    with open(filepath, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue

            if line.upper().startswith("CHAPTER:"):
                current_chapter = line[8:].strip()

            elif line.upper().startswith("Q:"):
                if q and q.get("answer") is not None:
                    questions.append(q)
                q = {"chapter": current_chapter,
                     "question": line[2:].strip(),
                     "choices": [],
                     "answer": None}

            elif len(line) >= 2 and line[0] in "1234" and line[1] == ":" and q is not None:
                q["choices"].append(line[2:].strip())

            elif line.upper().startswith("ANSWER:") and q is not None:
                ans = line[7:].strip()
                if ans in ("1", "2", "3", "4"):
                    q["answer"] = int(ans) - 1   # 0-indexed
                    questions.append(q)
                    q = None

            elif line.upper().startswith("EXPLANATION:") and questions:
                questions[-1]["explain"] = line[12:].strip()
            elif line.upper().startswith("EXPLAIN:") and questions:
                questions[-1]["explain"] = line[8:].strip()

    return questions


def discover_question_sets():
    base = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(base, "questions")
    sets = {}
    for path in sorted(glob.glob(os.path.join(folder, "*.txt"))):
        name = os.path.splitext(os.path.basename(path))[0].replace("_", " ").title()
        sets[name] = path
    return sets


# ─────────────────────────────────────────────
#  QUIZ APPLICATION
# ─────────────────────────────────────────────
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("History Quiz")
        self.root.geometry("820x660")
        self.root.resizable(True, True)
        self.root.configure(bg="#1a1a2e")

        self.all_questions = []
        self.queue = []          # remaining questions to ask
        self.missed = []         # questions answered wrong this pass
        self.current_q = None
        self.score = 0
        self.total_asked = 0
        self.answered = False
        self.answer_log = []

        self.chapter_filter = tk.StringVar(value="All Chapters")
        self.set_var = tk.StringVar()
        self.shuffle_var = tk.BooleanVar(value=True)

        self._setup_styles()
        self._build_menu_screen()

    # ── Styles ──────────────────────────────
    def _setup_styles(self):
        s = ttk.Style()
        s.theme_use("clam")
        s.configure("TCombobox",
                    fieldbackground="#16213e", background="#0f3460",
                    foreground="#e0e0e0", selectbackground="#e94560",
                    font=("Courier New", 11))
        s.configure("bar.Horizontal.TProgressbar",
                    troughcolor="#16213e", background="#e94560", thickness=6)

    # ── MENU SCREEN ──────────────────────────
    def _build_menu_screen(self):
        self._clear()
        self._unbind_keys()

        question_sets = discover_question_sets()
        if not question_sets:
            messagebox.showerror(
                "No Question Files Found",
                "No .txt files found in the 'questions' folder.\n"
                "Please add question files there and restart.")
            return
        self._question_sets = question_sets

        # Banner
        banner = tk.Frame(self.root, bg="#e94560", pady=14)
        banner.pack(fill="x")
        tk.Label(banner, text="📚  HISTORY QUIZ",
                 font=("Courier New", 22, "bold"),
                 bg="#e94560", fg="white").pack()
        tk.Label(banner,
                 text="1–4 to answer  •  any key to advance  •  missed questions repeat",
                 font=("Courier New", 10), bg="#e94560", fg="#ffe0e6").pack()

        # Card
        card = tk.Frame(self.root, bg="#16213e", padx=40, pady=30)
        card.pack(expand=True)

        tk.Label(card, text="Configure Your Quiz",
                 font=("Courier New", 15, "bold"),
                 bg="#16213e", fg="#e0e0e0"
                 ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Question set picker
        tk.Label(card, text="Question Set:", font=("Courier New", 11),
                 bg="#16213e", fg="#a0a0c0"
                 ).grid(row=1, column=0, sticky="w", padx=(0, 12))
        set_names = list(question_sets.keys())
        self.set_var.set(set_names[0])
        set_cb = ttk.Combobox(card, textvariable=self.set_var, values=set_names,
                              state="readonly", width=32, font=("Courier New", 11))
        set_cb.grid(row=1, column=1, pady=6, sticky="w")

        # Chapter filter
        tk.Label(card, text="Filter by Chapter:", font=("Courier New", 11),
                 bg="#16213e", fg="#a0a0c0"
                 ).grid(row=2, column=0, sticky="w", padx=(0, 12))
        self._chapter_cb = ttk.Combobox(card, textvariable=self.chapter_filter,
                                         state="readonly", width=32,
                                         font=("Courier New", 11))
        self._chapter_cb.grid(row=2, column=1, pady=6, sticky="w")

        # Shuffle
        tk.Checkbutton(card, text="Shuffle question order",
                       variable=self.shuffle_var,
                       bg="#16213e", fg="#a0a0c0", selectcolor="#0f3460",
                       activebackground="#16213e", activeforeground="#e94560",
                       font=("Courier New", 11)
                       ).grid(row=3, column=0, columnspan=2, pady=6, sticky="w")

        self._avail_label = tk.Label(card, text="",
                                     font=("Courier New", 10, "italic"),
                                     bg="#16213e", fg="#606080")
        self._avail_label.grid(row=4, column=0, columnspan=2, pady=(0, 20))

        self._load_set(set_names[0])
        set_cb.bind("<<ComboboxSelected>>",
                    lambda e: self._load_set(self.set_var.get()))
        self._chapter_cb.bind("<<ComboboxSelected>>",
                               lambda e: self._update_avail())

        tk.Button(card, text="▶  START QUIZ",
                  font=("Courier New", 14, "bold"),
                  bg="#e94560", fg="white",
                  activebackground="#c73652", activeforeground="white",
                  relief="flat", padx=30, pady=10, cursor="hand2",
                  command=self._start_quiz
                  ).grid(row=5, column=0, columnspan=2, pady=6)

    def _load_set(self, set_name):
        path = self._question_sets[set_name]
        try:
            self.all_questions = load_questions_from_file(path)
        except Exception as e:
            messagebox.showerror("Load Error", f"Could not load questions:\n{e}")
            self.all_questions = []
        chapters = ["All Chapters"] + sorted(
            set(q["chapter"] for q in self.all_questions))
        self._chapter_cb["values"] = chapters
        self.chapter_filter.set("All Chapters")
        self._update_avail()

    def _update_avail(self):
        ch = self.chapter_filter.get()
        pool = (self.all_questions if ch == "All Chapters"
                else [q for q in self.all_questions if q["chapter"] == ch])
        self._avail_label.config(
            text=f"{len(pool)} questions — all will be asked, missed ones repeat")

    # ── Start quiz ───────────────────────────
    def _start_quiz(self):
        ch = self.chapter_filter.get()
        pool = (self.all_questions if ch == "All Chapters"
                else [q for q in self.all_questions if q["chapter"] == ch])
        if not pool:
            messagebox.showwarning("No Questions",
                                   "No questions available for this selection.")
            return

        self.queue = random.sample(pool, len(pool)) if self.shuffle_var.get() else list(pool)
        self.missed = []
        self.score = 0
        self.total_asked = 0
        self.answer_log = []
        self._total_unique = len(self.queue)   # original question count

        self._build_quiz_screen()
        self._load_question()

    # ── QUIZ SCREEN ──────────────────────────
    def _build_quiz_screen(self):
        self._clear()
        self._unbind_keys()

        # Top bar
        top = tk.Frame(self.root, bg="#0f3460", pady=8, padx=16)
        top.pack(fill="x")
        self.progress_label = tk.Label(top, text="",
                                       font=("Courier New", 11),
                                       bg="#0f3460", fg="#a0c4ff")
        self.progress_label.pack(side="left")
        self.score_label = tk.Label(top, text="",
                                    font=("Courier New", 11, "bold"),
                                    bg="#0f3460", fg="#7dffb3")
        self.score_label.pack(side="right")

        # Progress bar (tracks unique questions answered correctly)
        self.pb_var = tk.DoubleVar(value=0)
        ttk.Progressbar(self.root, variable=self.pb_var,
                        maximum=self._total_unique,
                        style="bar.Horizontal.TProgressbar"
                        ).pack(fill="x")

        # "Repeat" badge — shown when question is a retry
        self.repeat_label = tk.Label(self.root, text="",
                                     font=("Courier New", 9, "bold"),
                                     bg="#1a1a2e", fg="#e94560")
        self.repeat_label.pack(anchor="w", padx=20, pady=(8, 0))

        # Chapter tag
        self.chapter_label = tk.Label(self.root, text="",
                                      font=("Courier New", 9),
                                      bg="#1a1a2e", fg="#606080")
        self.chapter_label.pack(anchor="w", padx=20)

        # Question
        q_frame = tk.Frame(self.root, bg="#16213e", padx=24, pady=18)
        q_frame.pack(fill="x", padx=20, pady=(4, 0))
        self.q_label = tk.Label(q_frame, text="",
                                font=("Courier New", 13, "bold"),
                                bg="#16213e", fg="#e8e8f0",
                                wraplength=740, justify="left")
        self.q_label.pack(anchor="w")

        # Choices
        self.btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.btn_frame.pack(fill="both", padx=20, pady=10, expand=True)
        self.choice_btns = []
        for i in range(4):
            btn = tk.Button(self.btn_frame, text="",
                            font=("Courier New", 11),
                            bg="#16213e", fg="#d0d0e8",
                            activebackground="#0f3460",
                            activeforeground="white",
                            relief="flat", anchor="w",
                            padx=16, pady=10,
                            wraplength=720, justify="left",
                            cursor="hand2",
                            command=lambda idx=i: self._check_answer(idx))
            btn.pack(fill="x", pady=4)
            self.choice_btns.append(btn)

        # Feedback
        self.feedback_label = tk.Label(self.root, text="",
                                       font=("Courier New", 12, "bold"),
                                       bg="#1a1a2e", fg="white")
        self.feedback_label.pack(pady=(0, 2))

        # Explanation (shown on wrong answer)
        self.explain_label = tk.Label(self.root, text="",
                                      font=("Courier New", 10, "italic"),
                                      bg="#1a1a2e", fg="#ffd700",
                                      wraplength=740, justify="left")
        self.explain_label.pack(padx=24, pady=(0, 2))

        # Hint
        self.hint_label = tk.Label(self.root, text="",
                                   font=("Courier New", 9, "italic"),
                                   bg="#1a1a2e", fg="#505070")
        self.hint_label.pack()

    # ── Load question ─────────────────────
    def _load_question(self):
        self.answered = False
        self.feedback_label.config(text="")
        self.explain_label.config(text="")
        self.hint_label.config(text="Press  1 · 2 · 3 · 4  to answer")
        self._unbind_keys()
        self._bind_answer_keys()

        self.current_q = self.queue.pop(0)
        q = self.current_q
        is_retry = q.get("_retry", False)

        remaining_unique = len([x for x in self.queue if not x.get("_retry")])
        correct_so_far = self.score
        missed_still = len([x for x in self.queue if x.get("_retry")]) + (1 if is_retry else 0)

        self.repeat_label.config(
            text="🔁  REPEAT — you missed this one earlier" if is_retry else "")
        self.chapter_label.config(text=q["chapter"])
        self.progress_label.config(
            text=f"Mastered: {correct_so_far}/{self._total_unique}  |  "
                 f"Remaining: {remaining_unique + (0 if is_retry else 1)}  |  "
                 f"Still need to repeat: {missed_still}")
        self.pb_var.set(correct_so_far)
        self.score_label.config(
            text=f"✅ {self.score}  ❌ {self.total_asked - self.score}")
        self.q_label.config(text=q["question"])

        for i, btn in enumerate(self.choice_btns):
            text = f"  {i+1}.  {q['choices'][i]}" if i < len(q["choices"]) else ""
            btn.config(text=text, bg="#16213e", fg="#d0d0e8",
                       state="normal", relief="flat")

    # ── Check answer ──────────────────────
    def _check_answer(self, idx):
        if self.answered:
            return
        self.answered = True
        self._unbind_keys()

        q = self.current_q
        correct_idx = q["answer"]
        self.total_asked += 1

        for btn in self.choice_btns:
            btn.config(state="disabled")

        if idx == correct_idx:
            # Only count as mastered if this is not a retry,
            # OR if it IS a retry (either way increment score once per unique correct)
            if not q.get("_retry"):
                self.score += 1
            else:
                self.score += 1   # they got the repeat right — mastered!
            self.choice_btns[idx].config(bg="#1a5c3a", fg="white", relief="groove")
            self.feedback_label.config(text="✅  Correct!", fg="#7dffb3")
            self.answer_log.append({
                "q": q["question"], "result": "✅ Correct",
                "your": q["choices"][idx],
                "correct": q["choices"][correct_idx]
            })
        else:
            self.choice_btns[idx].config(bg="#5c1a1a", fg="#ffaaaa", relief="groove")
            if correct_idx < len(self.choice_btns):
                self.choice_btns[correct_idx].config(
                    bg="#1a5c3a", fg="white", relief="groove")
            self.feedback_label.config(
                text=f"❌  Wrong — correct answer: {correct_idx + 1}",
                fg="#ff6b6b")
            self.answer_log.append({
                "q": q["question"], "result": "❌ Incorrect",
                "your": q["choices"][idx],
                "correct": q["choices"][correct_idx]
            })

        # Show explanation for every answer, right or wrong
        explanation = q.get("explain", "")
        if explanation:
            self.explain_label.config(text=f"💡  {explanation}")

            # Re-insert question at a random position later in the queue
            # (but not immediately — at least 2 spots away, or end of queue)
            retry_q = dict(q)
            retry_q["_retry"] = True
            insert_at = _random_reinsert_index(self.queue)
            self.queue.insert(insert_at, retry_q)

        self.pb_var.set(self.score)
        self.score_label.config(
            text=f"✅ {self.score}  ❌ {self.total_asked - self.score}")
        self.hint_label.config(text="Press any key to continue  →")
        self.root.after(300, self._bind_advance_key)

    # ── Next question ─────────────────────
    def _next_question(self, event=None):
        if not self.answered:
            return
        self._unbind_keys()
        if not self.queue:
            self._show_results()
        else:
            self._load_question()

    # ── RESULTS SCREEN ────────────────────
    def _show_results(self):
        self._clear()
        self._unbind_keys()

        total_unique = self._total_unique
        pct = round(self.score / total_unique * 100) if total_unique else 0
        color = ("#7dffb3" if pct >= 70 else
                 "#ffd700" if pct >= 50 else "#ff6b6b")
        grade = ("A" if pct >= 90 else "B" if pct >= 80 else
                 "C" if pct >= 70 else "D" if pct >= 60 else "F")

        banner = tk.Frame(self.root, bg="#0f3460", pady=16)
        banner.pack(fill="x")
        tk.Label(banner, text="📊  ALL QUESTIONS MASTERED!",
                 font=("Courier New", 20, "bold"),
                 bg="#0f3460", fg="white").pack()

        card = tk.Frame(self.root, bg="#16213e", padx=30, pady=20)
        card.pack(padx=40, pady=16, fill="x")

        tk.Label(card, text=f"{self.score} / {total_unique} correct on first try",
                 font=("Courier New", 22, "bold"),
                 bg="#16213e", fg=color).pack()
        tk.Label(card, text=f"{pct}%   Grade: {grade}",
                 font=("Courier New", 16), bg="#16213e", fg=color).pack(pady=2)
        tk.Label(card,
                 text=f"Total attempts (including repeats): {self.total_asked}",
                 font=("Courier New", 10), bg="#16213e", fg="#707090").pack(pady=2)

        msg = ("🏆 Excellent work!" if pct >= 90 else
               "👍 Good job!" if pct >= 70 else
               "📖 Keep studying!" if pct >= 50 else
               "📚 Review the material and try again!")
        tk.Label(card, text=msg, font=("Courier New", 12, "italic"),
                 bg="#16213e", fg="#a0a0c0").pack(pady=4)

        tk.Label(self.root, text="Answer Review (first attempts only):",
                 font=("Courier New", 11, "bold"),
                 bg="#1a1a2e", fg="#a0c4ff").pack(anchor="w", padx=40)

        rev = tk.Frame(self.root, bg="#1a1a2e")
        rev.pack(fill="both", expand=True, padx=40, pady=(4, 6))
        sb = tk.Scrollbar(rev)
        sb.pack(side="right", fill="y")
        txt = tk.Text(rev, font=("Courier New", 9), bg="#0d0d1a", fg="#c0c0d8",
                      yscrollcommand=sb.set, relief="flat", wrap="word",
                      padx=10, pady=6)
        txt.pack(fill="both", expand=True)
        sb.config(command=txt.yview)

        # Only show first attempt for each question
        seen = set()
        for entry in self.answer_log:
            qtext = entry["q"]
            if qtext in seen:
                continue
            seen.add(qtext)
            txt.insert("end", f"{entry['result']}  {qtext}\n")
            if entry["result"].startswith("❌"):
                txt.insert("end", f"   Your answer:    {entry['your']}\n")
                txt.insert("end", f"   Correct answer: {entry['correct']}\n\n")
            else:
                txt.insert("end", "\n")
        txt.config(state="disabled")

        row = tk.Frame(self.root, bg="#1a1a2e")
        row.pack(pady=6)
        tk.Button(row, text="🔁  Play Again",
                  font=("Courier New", 12, "bold"),
                  bg="#e94560", fg="white", relief="flat",
                  padx=20, pady=8, cursor="hand2",
                  command=self._start_quiz).pack(side="left", padx=8)
        tk.Button(row, text="🏠  Main Menu",
                  font=("Courier New", 12, "bold"),
                  bg="#0f3460", fg="white", relief="flat",
                  padx=20, pady=8, cursor="hand2",
                  command=self._build_menu_screen).pack(side="left", padx=8)

    # ── Key binding helpers ───────────────
    def _bind_answer_keys(self):
        for i, key in enumerate(("1", "2", "3", "4")):
            self.root.bind(key, lambda e, idx=i: self._check_answer(idx))
        for i, key in enumerate(("KP_1", "KP_2", "KP_3", "KP_4")):
            self.root.bind(f"<{key}>", lambda e, idx=i: self._check_answer(idx))

    def _bind_advance_key(self):
        self.root.bind("<Key>", self._next_question)

    def _unbind_keys(self):
        for key in ("1", "2", "3", "4", "<Key>"):
            try:
                self.root.unbind(key)
            except Exception:
                pass
        for key in ("<KP_1>", "<KP_2>", "<KP_3>", "<KP_4>"):
            try:
                self.root.unbind(key)
            except Exception:
                pass

    # ── Utility ───────────────────────────
    def _clear(self):
        for w in self.root.winfo_children():
            w.destroy()


def _random_reinsert_index(queue):
    """Pick a random insertion point that is at least 2 slots away from the front."""
    min_idx = min(2, len(queue))
    max_idx = len(queue)
    if min_idx >= max_idx:
        return max_idx
    return random.randint(min_idx, max_idx)


# ─────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()