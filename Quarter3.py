import tkinter as tk
from tkinter import ttk, messagebox
import random
import json

# ─────────────────────────────────────────────
#  QUESTION BANK  (75 questions)
# ─────────────────────────────────────────────
ALL_QUESTIONS = [
    # ── Chapter 16 – Capital & Labor ──
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "What is Taylorism?",
        "choices": ["A) A theory of Social Darwinism", "B) Scientific management focused on factory efficiency", "C) A labor union organizing strategy", "D) A government regulation of big business"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "By 1913, U.S. industrial output exceeded which combination of countries?",
        "choices": ["A) Russia, Japan, and Italy", "B) Britain, France, and Germany combined", "C) Canada, Mexico, and Australia combined", "D) Spain, Portugal, and the Netherlands combined"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "What was the first billion-dollar corporation in the United States?",
        "choices": ["A) Standard Oil", "B) Carnegie Steel", "C) U.S. Steel", "D) Pennsylvania Railroad"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "According to late 1800s wealth distribution, roughly what percentage of wealth was controlled by the richest 10%?",
        "choices": ["A) 50%", "B) 70%", "C) 90%", "D) 99%"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "Social Darwinism applied to economics argued that:",
        "choices": ["A) The government should protect workers from exploitation", "B) Helping the poor weakens society and government should not interfere in business", "C) Wealthy industrialists must donate half their fortunes", "D) Competition should be regulated to ensure fairness"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "Approximately how many strikes occurred in the late 1800s?",
        "choices": ["A) 2,000", "B) 10,000", "C) Over 20,000", "D) 50,000"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "Which event significantly hurt the Knights of Labor's reputation?",
        "choices": ["A) The Pullman Strike", "B) The Homestead Strike", "C) The Haymarket Affair", "D) The Great Railroad Strike"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "How did the Knights of Labor differ from the American Federation of Labor (AFL)?",
        "choices": ["A) Knights accepted only skilled workers; AFL accepted everyone", "B) Knights were reform-minded with broad membership; AFL focused on skilled workers, wages & hours", "C) Knights focused on wages only; AFL sought broad social reform", "D) There was no significant difference between the two"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "The Populist Party (People's Party) was primarily formed by:",
        "choices": ["A) Urban factory workers", "B) Small farmers", "C) Wealthy industrialists seeking reform", "D) Immigrant communities in Northern cities"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "Which of the following was NOT part of the Omaha Platform?",
        "choices": ["A) Nationalize railroads", "B) Free silver to increase inflation", "C) Government loans to farmers (subtreasury system)", "D) High protective tariffs on manufactured goods"],
        "answer": "D"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "Why did the Populist Party's Southern coalition fail?",
        "choices": ["A) Farmers preferred the Republican Party", "B) Southern unity failed due to racial conflict", "C) The party lacked a clear economic platform", "D) Southern farmers were too prosperous to support Populism"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "In the 1896 presidential election, William Jennings Bryan ran primarily on which issue?",
        "choices": ["A) Anti-imperialism", "B) Protective tariffs", "C) Free silver (bimetallism)", "D) Nationalization of railroads"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "Which of the following helped William McKinley win the 1896 election?",
        "choices": ["A) Strong support from Southern farmers", "B) More campaign money, Northeast support, and better voter turnout", "C) A promise to nationalize the railroads", "D) Support from labor unions and immigrants"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "\"Interchangeable parts\" in industrial manufacturing primarily led to:",
        "choices": ["A) Higher wages for skilled craftsmen", "B) Decreased production speed", "C) Increased production and efficiency", "D) Stricter government regulation"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 16 – Capital & Labor",
        "question": "The term 'free silver' in the Populist Platform referred to:",
        "choices": ["A) Eliminating the silver tax", "B) Freely distributing silver coins to the poor", "C) Coining silver at a fixed ratio to gold to increase money supply and inflation", "D) Selling federal silver reserves to pay off national debt"],
        "answer": "C"
    },

    # ── Chapter 17 – Conquering the West ──
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "Under the Homestead Act, settlers received 160 acres of land after:",
        "choices": ["A) Paying a flat fee of $500", "B) Serving in the military for 2 years", "C) Living on and farming the land for 5 years", "D) Obtaining approval from a federal land office committee"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "What was the MAIN reason people moved West during the late 1800s?",
        "choices": ["A) Escaping industrial pollution in Eastern cities", "B) Land for farming", "C) Joining mining operations", "D) Following religious communities"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "How were transcontinental railroads primarily funded?",
        "choices": ["A) Entirely by private investors with no government help", "B) Federal land grants and loans", "C) State bond measures passed by voters", "D) Taxes on imported European goods"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "Which city became the key railroad hub in the late 1800s?",
        "choices": ["A) St. Louis", "B) New York", "C) Chicago", "D) Kansas City"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "Compared to homesteaders, how much land did railroad companies receive from the federal government?",
        "choices": ["A) About the same amount", "B) Significantly less land", "C) More land than homesteaders", "D) No land — only cash subsidies"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "What did the Ghost Dance promise Native Americans?",
        "choices": ["A) Safe passage to Canada", "B) Return of buffalo, return of ancestors, and disappearance of white settlers", "C) Government payment for lost reservation lands", "D) Restoration of tribal sovereignty under U.S. law"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "What was the purpose of the Dawes Act regarding Native American land?",
        "choices": ["A) Create new reservations in the West", "B) Return stolen tribal lands to Native Americans", "C) Break reservations into individual allotments for assimilation", "D) Fund Native American schools and colleges"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "American cowboys adapted many of their practices from which cultural group?",
        "choices": ["A) Spanish conquistadors", "B) Mexican vaqueros", "C) Native American horsemen", "D) British ranchers in Texas"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "Approximately what percentage of early rodeo contestants were women?",
        "choices": ["A) Less than 1%", "B) About 5%", "C) About 20%", "D) About 35%"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "Wild West shows were popular in the late 1800s for all of the following reasons EXCEPT:",
        "choices": ["A) Anxiety about changing masculinity", "B) Fear that Native cultures were disappearing", "C) Clear good vs. evil storytelling", "D) Promoting real historical accuracy about the frontier"],
        "answer": "D"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "According to Turner's Frontier Thesis, the frontier shaped which aspects of American identity?",
        "choices": ["A) Religious devotion and missionary spirit", "B) Democracy, independence, and national character", "C) Industrial innovation and corporate culture", "D) Military strength and expansionist ideology"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 17 – Conquering the West",
        "question": "What policy did the U.S. government force on Native American tribes regarding their land?",
        "choices": ["A) Tribes could keep land but had to pay taxes", "B) Tribes were offered citizenship if they sold their lands", "C) Tribes were required to move to reservations", "D) Tribes could vote on keeping or selling their lands"],
        "answer": "C"
    },

    # ── Chapter 18 – Industrial America ──
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "Which city was the largest meatpacking center in late 19th-century America?",
        "choices": ["A) Kansas City", "B) St. Louis", "C) Chicago", "D) Cincinnati"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "The 1920 Census revealed a major demographic milestone. What was it?",
        "choices": ["A) The U.S. population exceeded 100 million", "B) The majority of Americans lived in cities for the first time", "C) Immigration surpassed natural population growth", "D) Women officially outnumbered men in the workforce"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "By 1890, approximately what percentage of Northern city residents were immigrants or children of immigrants?",
        "choices": ["A) 20%", "B) 40%", "C) 60%", "D) 80%"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "Politically, immigrants in the late 1800s mostly voted for which party?",
        "choices": ["A) Republican", "B) Democratic", "C) Populist", "D) Progressive"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "Immigrant communities maintained their cultural identity through all of the following EXCEPT:",
        "choices": ["A) Mutual-aid societies", "B) Parish churches", "C) Workmen's clubs", "D) Rotary clubs"],
        "answer": "D"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "After Reconstruction, the Southern economy was primarily characterized by:",
        "choices": ["A) Rapid industrial growth rivaling the North", "B) Mostly agricultural economy despite 'New South' rhetoric", "C) A booming textile industry funded by Northern investors", "D) Economic equality between Black and white Southerners"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "Approximately how many African Americans were lynched between 1880 and 1950?",
        "choices": ["A) About 500", "B) About 1,500", "C) About 3,000", "D) About 5,000"],
        "answer": "D"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "Who led the anti-lynching campaign in the late 1800s?",
        "choices": ["A) Booker T. Washington", "B) Frederick Douglass", "C) Ida B. Wells", "D) W.E.B. Du Bois"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "Black disenfranchisement in the South was achieved through all of the following EXCEPT:",
        "choices": ["A) Poll taxes", "B) Literacy tests", "C) Violence and intimidation", "D) Property ownership requirements for running for office only"],
        "answer": "D"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "The 'Lost Cause' ideology did which of the following?",
        "choices": ["A) Celebrated Union victory and abolition", "B) Romanticized the Confederacy and its cause", "C) Argued for reparations to formerly enslaved people", "D) Promoted reconciliation between North and South"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "\"Muscular Christianity\" linked which two ideas?",
        "choices": ["A) Church attendance and political activism", "B) Physical strength and moral virtue", "C) Military service and spiritual salvation", "D) Temperance and physical fitness"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "The 'Tainted Money Debate' centered on whether churches should accept donations from:",
        "choices": ["A) Foreign governments", "B) John D. Rockefeller", "C) Labor union funds", "D) Federal government grants"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "Charlotte Perkins Gilman and Kate Chopin are associated with which intellectual movement?",
        "choices": ["A) Promoting Social Darwinism", "B) Supporting Muscular Christianity", "C) Critiquing gender roles in American society", "D) Defending the Lost Cause ideology"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 18 – Industrial America",
        "question": "What did 'New South' boosters want for the South after Reconstruction?",
        "choices": ["A) A return to plantation agriculture", "B) Full racial equality with economic reform", "C) Industrial development while maintaining white supremacy", "D) Political reunification with the North under Republican leadership"],
        "answer": "C"
    },

    # ── Chapter 19 – American Empire ──
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "When did the United States begin trading with China?",
        "choices": ["A) 1776", "B) 1784", "C) 1812", "D) 1850"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "The Guano Islands Act of 1856 allowed Americans to:",
        "choices": ["A) Establish military bases in the Pacific", "B) Claim uninhabited islands containing guano (bird droppings used as fertilizer)", "C) Annex any island within 500 miles of U.S. territory", "D) Tax foreign ships traveling through U.S.-claimed waters"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "What connected the United States and Brazil economically in the early 1800s?",
        "choices": ["A) Cotton trade agreements", "B) Slave economies", "C) Shared railroad infrastructure", "D) Joint military defense pacts"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "The Open Door Policy was primarily concerned with:",
        "choices": ["A) Allowing unrestricted immigration from Asia", "B) Equal access to Chinese markets for all major powers", "C) Opening trade routes through the Panama Canal", "D) Giving U.S. companies free access to Latin American resources"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "During the Boxer Rebellion, the United States:",
        "choices": ["A) Remained neutral and did not intervene", "B) Sided with Chinese nationalists against foreign powers", "C) Joined an international military force to suppress the rebellion", "D) Used the rebellion as justification to annex parts of China"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "In the 1800s, U.S. interests in the Middle East were primarily focused on:",
        "choices": ["A) Oil reserves and pipelines", "B) Military bases and strategic ports", "C) Religion, education, and trade routes", "D) Suppressing Ottoman imperialism"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "When did the U.S. gain control of the Philippines?",
        "choices": ["A) 1890", "B) 1895", "C) 1898", "D) 1902"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "After the U.S. gained the Philippines, Filipinos:",
        "choices": ["A) Welcomed U.S. rule as liberators from Spain", "B) Fought for their independence against U.S. forces", "C) Voted to become a U.S. territory peacefully", "D) Allied with Japan against the United States"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "What was the Roosevelt Corollary to the Monroe Doctrine?",
        "choices": ["A) The U.S. would assist European nations in colonizing Africa", "B) The U.S. had the right to intervene in Latin American countries to maintain order", "C) Latin American nations must pay tribute to the U.S. for military protection", "D) The U.S. would extend the Monroe Doctrine to cover Asia and the Pacific"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "Theodore Roosevelt built a powerful 'blue water' navy primarily to:",
        "choices": ["A) Protect coastal fishing rights", "B) Project U.S. power globally across open oceans", "C) Defend against a potential British invasion", "D) Support the transatlantic slave trade"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "Why did President Wilson order an invasion of Veracruz, Mexico?",
        "choices": ["A) Mexico refused to pay U.S. debts", "B) Mexican forces crossed into Texas", "C) Following the arrest of U.S. sailors by Mexican authorities", "D) To prevent a German military alliance with Mexico"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "Which immigrant group faced the STRICTEST immigration restrictions in the late 1800s?",
        "choices": ["A) Irish Catholics", "B) Southern Europeans", "C) Chinese immigrants", "D) Eastern European Jews"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "During the late 1800s, immigration from Western Europe:",
        "choices": ["A) Increased dramatically", "B) Remained steady", "C) Decreased", "D) Was banned by Congress"],
        "answer": "C"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "Most Catholic bishops in the United States in the late 1800s were of what ethnicity?",
        "choices": ["A) Italian", "B) German", "C) Polish", "D) Irish"],
        "answer": "D"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "Catholic 'Americanists' believed which of the following?",
        "choices": ["A) Immigrants should maintain ethnic parishes and resist assimilation", "B) Immigrants should assimilate, ethnic parishes should close, and church-state separation benefits Catholics", "C) The U.S. government should fund Catholic schools", "D) Catholics should form their own political party"],
        "answer": "B"
    },
    {
        "chapter": "Ch. 19 – American Empire",
        "question": "The Spanish-American War began primarily due to:",
        "choices": ["A) The assassination of a U.S. diplomat in Cuba", "B) Spain's attack on Florida", "C) Confusion and escalating tensions, not a single assassination", "D) The sinking of a U.S. battleship by Spanish forces in open waters"],
        "answer": "C"
    },

    # ── Cross-Chapter / Synthesis ──
    {
        "chapter": "Synthesis",
        "question": "Which of the following BEST represents a similarity between the Knights of Labor and the Populist Party?",
        "choices": ["A) Both focused exclusively on skilled workers", "B) Both sought broad economic reform and challenged concentrated wealth", "C) Both supported the gold standard", "D) Both were strongest in Northeastern industrial cities"],
        "answer": "B"
    },
    {
        "chapter": "Synthesis",
        "question": "Social Darwinism and the 'Lost Cause' ideology both served to:",
        "choices": ["A) Justify existing social hierarchies and resist reform", "B) Promote equality and democratic values", "C) Strengthen labor unions and farmer movements", "D) Encourage government intervention in the economy"],
        "answer": "A"
    },
    {
        "chapter": "Synthesis",
        "question": "The Dawes Act and the Chinese Exclusion Act both reflect which broader late 19th-century trend?",
        "choices": ["A) American generosity toward minority groups", "B) Federal government policies that restricted or undermined non-white groups", "C) Growing immigration from East Asia", "D) Expansion of civil rights following the Civil War"],
        "answer": "B"
    },
    {
        "chapter": "Synthesis",
        "question": "Turner's Frontier Thesis was written in 1893, just as the frontier was declared closed. This timing suggests the thesis was partly a response to:",
        "choices": ["A) Anger over the Dawes Act's effects on Native Americans", "B) Anxiety about American identity now that westward expansion had ended", "C) Celebration of U.S. military victories over Native tribes", "D) Criticism of railroad companies' land grabs"],
        "answer": "B"
    },
    {
        "chapter": "Synthesis",
        "question": "The Roosevelt Corollary and the Open Door Policy both reflect which U.S. foreign policy goal?",
        "choices": ["A) Isolationism and non-intervention abroad", "B) Asserting U.S. economic and political power in foreign regions", "C) Building military alliances with European powers", "D) Spreading democracy through free elections"],
        "answer": "B"
    },
    {
        "chapter": "Synthesis",
        "question": "Which pairing of individuals and their causes is CORRECT?",
        "choices": ["A) Ida B. Wells – women's suffrage; Charlotte Perkins Gilman – anti-lynching", "B) Ida B. Wells – anti-lynching; Charlotte Perkins Gilman – gender role critique", "C) Ida B. Wells – labor rights; Kate Chopin – immigration reform", "D) Kate Chopin – Social Darwinism; Ida B. Wells – Populism"],
        "answer": "B"
    },
    {
        "chapter": "Synthesis",
        "question": "The subtreasury system proposed by the Populists was designed to help farmers by:",
        "choices": ["A) Eliminating all farm debt", "B) Allowing farmers to store crops and take government loans against them", "C) Setting minimum prices for agricultural goods", "D) Distributing unused federal land to poor farmers"],
        "answer": "B"
    },
    {
        "chapter": "Synthesis",
        "question": "Which of the following BEST explains why immigrants voted Democratic in the late 1800s?",
        "choices": ["A) Democrats promised to end all immigration restrictions", "B) Democratic machines in cities provided jobs, housing, and social services to immigrants", "C) Republicans actively excluded immigrants from voting", "D) Immigrants were required by law to register with a political party upon arrival"],
        "answer": "B"
    },
    {
        "chapter": "Synthesis",
        "question": "Both the Homestead Act and the Dawes Act involved the distribution of land. How did their effects differ?",
        "choices": ["A) Homestead Act helped white settlers gain land; Dawes Act broke up Native American tribal lands", "B) Both acts benefited Native Americans equally", "C) Homestead Act was for Native Americans; Dawes Act was for settlers", "D) Both acts gave land only to railroad companies"],
        "answer": "A"
    },
    {
        "chapter": "Synthesis",
        "question": "The late 1800s saw both massive industrial growth AND major labor unrest. What is the BEST explanation for this apparent contradiction?",
        "choices": ["A) Workers were satisfied but struck anyway to gain political power", "B) Industrial growth concentrated wealth at the top while workers faced dangerous conditions and low wages", "C) Labor unions caused industrial decline by demanding too much", "D) The government encouraged strikes to slow monopoly growth"],
        "answer": "B"
    },
    {
        "chapter": "Synthesis",
        "question": "Which of the following is the BEST example of U.S. imperialism in the late 1800s / early 1900s?",
        "choices": ["A) The Homestead Act opening Western lands to settlers", "B) The U.S. acquiring the Philippines after the Spanish-American War", "C) The formation of the AFL to protect American workers", "D) The passage of the Chinese Exclusion Act"],
        "answer": "B"
    },
    {
        "chapter": "Synthesis",
        "question": "\"New South\" boosters wanted industrialization, yet the South remained largely agricultural. What is the BEST explanation?",
        "choices": ["A) Southern workers refused to work in factories", "B) The racial caste system and lack of capital investment stunted industrial development", "C) The federal government blocked Southern industrial growth", "D) Southern states had no access to coal or iron for manufacturing"],
        "answer": "B"
    },
    {
        "chapter": "Synthesis",
        "question": "All of the following contributed to U.S. westward expansion EXCEPT:",
        "choices": ["A) Federal land grants to railroad companies", "B) The Homestead Act offering free land to settlers", "C) The Dawes Act redistributing Native American lands", "D) The Open Door Policy opening Pacific trade routes"],
        "answer": "D"
    },
]


# ─────────────────────────────────────────────
#  QUIZ APPLICATION
# ─────────────────────────────────────────────
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 History Quiz – Chapters 16–19")
        self.root.geometry("820x640")
        self.root.resizable(True, True)
        self.root.configure(bg="#1a1a2e")

        self.questions = []
        self.current_idx = 0
        self.score = 0
        self.answered = False
        self.selected_var = tk.StringVar()
        self.chapter_filter = tk.StringVar(value="All Chapters")
        self.answer_log = []

        self._setup_styles()
        self._build_menu_screen()

    # ── Styles ──────────────────────────────
    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox",
                        fieldbackground="#16213e",
                        background="#0f3460",
                        foreground="#e0e0e0",
                        selectbackground="#e94560",
                        font=("Courier New", 11))

    # ── MENU SCREEN ──────────────────────────
    def _build_menu_screen(self):
        self._clear()

        # Title banner
        banner = tk.Frame(self.root, bg="#e94560", pady=14)
        banner.pack(fill="x")
        tk.Label(banner, text="📚  U.S. HISTORY QUIZ", font=("Courier New", 22, "bold"),
                 bg="#e94560", fg="white").pack()
        tk.Label(banner, text="Chapters 16–19  •  Industrialization through Imperialism",
                 font=("Courier New", 11), bg="#e94560", fg="#ffe0e6").pack()

        # Card
        card = tk.Frame(self.root, bg="#16213e", bd=0, padx=40, pady=30)
        card.pack(expand=True)

        tk.Label(card, text="Configure Your Quiz", font=("Courier New", 15, "bold"),
                 bg="#16213e", fg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Chapter filter
        tk.Label(card, text="Filter by Chapter:", font=("Courier New", 11),
                 bg="#16213e", fg="#a0a0c0").grid(row=1, column=0, sticky="w", padx=(0, 12))
        chapters = ["All Chapters"] + sorted(set(q["chapter"] for q in ALL_QUESTIONS))
        cb = ttk.Combobox(card, textvariable=self.chapter_filter, values=chapters,
                          state="readonly", width=30, font=("Courier New", 11))
        cb.grid(row=1, column=1, pady=6, sticky="w")

        # Number of questions
        tk.Label(card, text="Number of Questions:", font=("Courier New", 11),
                 bg="#16213e", fg="#a0a0c0").grid(row=2, column=0, sticky="w", padx=(0, 12))
        self.num_q_var = tk.IntVar(value=20)
        num_spin = tk.Spinbox(card, from_=5, to=len(ALL_QUESTIONS), increment=5,
                              textvariable=self.num_q_var, width=6,
                              bg="#0f3460", fg="#e0e0e0", font=("Courier New", 13),
                              buttonbackground="#e94560", relief="flat")
        num_spin.grid(row=2, column=1, pady=6, sticky="w")

        # Shuffle toggle
        self.shuffle_var = tk.BooleanVar(value=True)
        tk.Checkbutton(card, text="Shuffle Questions", variable=self.shuffle_var,
                       bg="#16213e", fg="#a0a0c0", selectcolor="#0f3460",
                       activebackground="#16213e", activeforeground="#e94560",
                       font=("Courier New", 11)).grid(row=3, column=0, columnspan=2,
                                                       pady=6, sticky="w")

        # Total available label
        self.avail_label = tk.Label(card, text="", font=("Courier New", 10, "italic"),
                                    bg="#16213e", fg="#606080")
        self.avail_label.grid(row=4, column=0, columnspan=2, pady=(0, 20))
        self._update_avail_label()
        cb.bind("<<ComboboxSelected>>", lambda e: self._update_avail_label())

        # Start button
        start_btn = tk.Button(card, text="▶  START QUIZ",
                              font=("Courier New", 14, "bold"),
                              bg="#e94560", fg="white", activebackground="#c73652",
                              activeforeground="white", relief="flat",
                              padx=30, pady=10, cursor="hand2",
                              command=self._start_quiz)
        start_btn.grid(row=5, column=0, columnspan=2, pady=6)

    def _update_avail_label(self):
        ch = self.chapter_filter.get()
        pool = ALL_QUESTIONS if ch == "All Chapters" else [q for q in ALL_QUESTIONS if q["chapter"] == ch]
        self.avail_label.config(text=f"{len(pool)} questions available for this selection")

    # ── Start / Build question list ──────────
    def _start_quiz(self):
        ch = self.chapter_filter.get()
        pool = ALL_QUESTIONS if ch == "All Chapters" else [q for q in ALL_QUESTIONS if q["chapter"] == ch]
        if self.shuffle_var.get():
            pool = random.sample(pool, min(self.num_q_var.get(), len(pool)))
        else:
            pool = pool[:self.num_q_var.get()]
        self.questions = pool
        self.current_idx = 0
        self.score = 0
        self.answer_log = []
        self._build_quiz_screen()
        self._load_question()

    # ── QUIZ SCREEN ──────────────────────────
    def _build_quiz_screen(self):
        self._clear()

        # Top bar
        top = tk.Frame(self.root, bg="#0f3460", pady=8, padx=16)
        top.pack(fill="x")
        self.progress_label = tk.Label(top, text="", font=("Courier New", 11),
                                       bg="#0f3460", fg="#a0c4ff")
        self.progress_label.pack(side="left")
        self.score_label = tk.Label(top, text="Score: 0", font=("Courier New", 11, "bold"),
                                    bg="#0f3460", fg="#7dffb3")
        self.score_label.pack(side="right")

        # Progress bar
        self.pb_var = tk.DoubleVar(value=0)
        self.pb = ttk.Progressbar(self.root, variable=self.pb_var, maximum=len(self.questions),
                                  style="green.Horizontal.TProgressbar")
        ttk.Style().configure("green.Horizontal.TProgressbar",
                              troughcolor="#16213e", background="#e94560", thickness=6)
        self.pb.pack(fill="x")

        # Chapter tag
        self.chapter_label = tk.Label(self.root, text="", font=("Courier New", 9),
                                      bg="#1a1a2e", fg="#606080")
        self.chapter_label.pack(anchor="w", padx=20, pady=(10, 0))

        # Question
        q_frame = tk.Frame(self.root, bg="#16213e", padx=24, pady=18)
        q_frame.pack(fill="x", padx=20, pady=(4, 0))
        self.q_label = tk.Label(q_frame, text="", font=("Courier New", 13, "bold"),
                                bg="#16213e", fg="#e8e8f0", wraplength=740, justify="left")
        self.q_label.pack(anchor="w")

        # Answer choices
        self.btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.btn_frame.pack(fill="both", padx=20, pady=10, expand=True)
        self.choice_btns = []
        for i in range(4):
            btn = tk.Button(self.btn_frame, text="", font=("Courier New", 11),
                            bg="#16213e", fg="#d0d0e8", activebackground="#0f3460",
                            activeforeground="white", relief="flat", anchor="w",
                            padx=16, pady=10, wraplength=720, justify="left",
                            cursor="hand2",
                            command=lambda idx=i: self._check_answer(idx))
            btn.pack(fill="x", pady=4)
            self.choice_btns.append(btn)

        # Feedback label
        self.feedback_label = tk.Label(self.root, text="", font=("Courier New", 12, "bold"),
                                       bg="#1a1a2e", fg="white")
        self.feedback_label.pack(pady=(0, 4))

        # Explanation label
        self.explain_label = tk.Label(self.root, text="", font=("Courier New", 10, "italic"),
                                      bg="#1a1a2e", fg="#909090", wraplength=760)
        self.explain_label.pack()

        # Next button
        self.next_btn = tk.Button(self.root, text="NEXT  →",
                                  font=("Courier New", 12, "bold"),
                                  bg="#e94560", fg="white",
                                  activebackground="#c73652", activeforeground="white",
                                  relief="flat", padx=24, pady=8, cursor="hand2",
                                  command=self._next_question, state="disabled")
        self.next_btn.pack(pady=8)

    # ── Load question ──────────────────────
    def _load_question(self):
        self.answered = False
        self.feedback_label.config(text="")
        self.explain_label.config(text="")
        self.next_btn.config(state="disabled")

        q = self.questions[self.current_idx]
        total = len(self.questions)

        self.progress_label.config(text=f"Question {self.current_idx + 1} / {total}")
        self.pb_var.set(self.current_idx)
        self.score_label.config(text=f"Score: {self.score}/{self.current_idx}")
        self.chapter_label.config(text=q["chapter"])
        self.q_label.config(text=q["question"])

        for i, btn in enumerate(self.choice_btns):
            btn.config(text=q["choices"][i], bg="#16213e", fg="#d0d0e8",
                       state="normal", relief="flat")

    # ── Check answer ──────────────────────
    def _check_answer(self, idx):
        if self.answered:
            return
        self.answered = True

        q = self.questions[self.current_idx]
        chosen_letter = ["A", "B", "C", "D"][idx]
        correct_letter = q["answer"]
        correct_idx = ["A", "B", "C", "D"].index(correct_letter)

        # Disable all buttons
        for btn in self.choice_btns:
            btn.config(state="disabled")

        if chosen_letter == correct_letter:
            self.score += 1
            self.choice_btns[idx].config(bg="#1a5c3a", fg="white", relief="groove")
            self.feedback_label.config(text="✅  Correct!", fg="#7dffb3")
            self.answer_log.append({"q": q["question"], "result": "✅ Correct",
                                     "your": q["choices"][idx], "correct": q["choices"][correct_idx]})
        else:
            self.choice_btns[idx].config(bg="#5c1a1a", fg="#ffaaaa", relief="groove")
            self.choice_btns[correct_idx].config(bg="#1a5c3a", fg="white", relief="groove")
            self.feedback_label.config(text=f"❌  Incorrect. Correct answer: {correct_letter}", fg="#ff6b6b")
            self.answer_log.append({"q": q["question"], "result": "❌ Incorrect",
                                     "your": q["choices"][idx], "correct": q["choices"][correct_idx]})

        self.score_label.config(text=f"Score: {self.score}/{self.current_idx + 1}")
        self.next_btn.config(state="normal")

    # ── Next question ──────────────────────
    def _next_question(self):
        self.current_idx += 1
        if self.current_idx >= len(self.questions):
            self._show_results()
        else:
            self._load_question()

    # ── RESULTS SCREEN ────────────────────
    def _show_results(self):
        self._clear()
        total = len(self.questions)
        pct = round(self.score / total * 100)

        color = "#7dffb3" if pct >= 70 else "#ffd700" if pct >= 50 else "#ff6b6b"
        grade = "A" if pct >= 90 else "B" if pct >= 80 else "C" if pct >= 70 else "D" if pct >= 60 else "F"

        # Banner
        banner = tk.Frame(self.root, bg="#0f3460", pady=16)
        banner.pack(fill="x")
        tk.Label(banner, text="📊  QUIZ COMPLETE", font=("Courier New", 20, "bold"),
                 bg="#0f3460", fg="white").pack()

        # Score card
        card = tk.Frame(self.root, bg="#16213e", padx=30, pady=20)
        card.pack(padx=40, pady=16, fill="x")

        tk.Label(card, text=f"{self.score}  /  {total}", font=("Courier New", 36, "bold"),
                 bg="#16213e", fg=color).pack()
        tk.Label(card, text=f"{pct}%   Grade: {grade}", font=("Courier New", 16),
                 bg="#16213e", fg=color).pack(pady=4)

        msg = ("🏆 Excellent work!" if pct >= 90 else
               "👍 Good job!" if pct >= 70 else
               "📖 Keep studying – you've got this!" if pct >= 50 else
               "📚 Review the study guide and try again!")
        tk.Label(card, text=msg, font=("Courier New", 12, "italic"),
                 bg="#16213e", fg="#a0a0c0").pack(pady=4)

        # Review scroll area
        tk.Label(self.root, text="Answer Review:", font=("Courier New", 11, "bold"),
                 bg="#1a1a2e", fg="#a0c4ff").pack(anchor="w", padx=40)

        review_frame = tk.Frame(self.root, bg="#1a1a2e")
        review_frame.pack(fill="both", expand=True, padx=40, pady=(4, 10))

        scroll = tk.Scrollbar(review_frame)
        scroll.pack(side="right", fill="y")
        listbox = tk.Text(review_frame, font=("Courier New", 9), bg="#0d0d1a", fg="#c0c0d8",
                          yscrollcommand=scroll.set, relief="flat", wrap="word",
                          padx=10, pady=6)
        listbox.pack(fill="both", expand=True)
        scroll.config(command=listbox.yview)

        for entry in self.answer_log:
            listbox.insert("end", f"{entry['result']}  {entry['q']}\n")
            if entry['result'].startswith("❌"):
                listbox.insert("end", f"   Your answer:    {entry['your']}\n")
                listbox.insert("end", f"   Correct answer: {entry['correct']}\n\n")
            else:
                listbox.insert("end", "\n")
        listbox.config(state="disabled")

        # Buttons
        btn_row = tk.Frame(self.root, bg="#1a1a2e")
        btn_row.pack(pady=8)
        tk.Button(btn_row, text="🔁  Try Again", font=("Courier New", 12, "bold"),
                  bg="#e94560", fg="white", relief="flat", padx=20, pady=8,
                  cursor="hand2", command=self._start_quiz).pack(side="left", padx=8)
        tk.Button(btn_row, text="🏠  Main Menu", font=("Courier New", 12, "bold"),
                  bg="#0f3460", fg="white", relief="flat", padx=20, pady=8,
                  cursor="hand2", command=self._build_menu_screen).pack(side="left", padx=8)

    # ── Utility ───────────────────────────
    def _clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()