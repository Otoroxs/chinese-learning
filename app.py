import html
import random

import streamlit as st

# ============================================================
# Chinese Flashcards — Native Streamlit App
# Replace your entire app.py with this file.
#
# Changes in this version:
# 1. Shuffle now really shuffles and does not reset back to the first card.
# 2. "Usage → Hanzi" and "English → Hanzi" use readable text sizes,
#    instead of the giant Hanzi font.
# ============================================================

st.set_page_config(
    page_title="Chinese Flashcards",
    page_icon="🀄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Flashcard data
# -----------------------------
CARDS = [
    {
        "hanzi": "上网",
        "pinyin": "shàng wǎng",
        "english": "to go online; use the internet",
        "category": "Technology",
        "part": "verb-object phrase",
        "usage": "Use 上网 when someone uses the internet in general. 网 is already the object, so you usually do not add another object after it.",
        "examples": ["我晚上上网。— I go online at night.", "你喜欢上网吗？— Do you like going online?"],
        "hint": "上 = get on; 网 = web/net → get on the web.",
    },
    {
        "hanzi": "上课",
        "pinyin": "shàng kè",
        "english": "to attend class; to have class",
        "category": "School",
        "part": "verb-object phrase",
        "usage": "Use 上课 when someone is in class or attends class. The opposite is 下课, class ends.",
        "examples": ["我九点上课。— I have class at 9.", "我们在教室上课。— We have class in the classroom."],
        "hint": "上 = start/attend; 课 = class.",
    },
    {
        "hanzi": "下课",
        "pinyin": "xià kè",
        "english": "class ends; to finish class",
        "category": "School",
        "part": "verb-object phrase",
        "usage": "Use 下课 when class is dismissed or finished.",
        "examples": ["几点下课？— What time does class end?", "下课以后我去吃饭。— After class I go eat."],
        "hint": "下 = down/off; class comes down/ends.",
    },
    {
        "hanzi": "查",
        "pinyin": "chá",
        "english": "to check; look up",
        "category": "Study",
        "part": "verb",
        "usage": "Often used in 查资料, to research information, and 查词典, to look something up in a dictionary.",
        "examples": ["我查词典。— I look it up in the dictionary.", "他在网上查资料。— He researches information online."],
        "hint": "查 is the action of checking or searching.",
    },
    {
        "hanzi": "发",
        "pinyin": "fā",
        "english": "to send; issue",
        "category": "Communication",
        "part": "verb",
        "usage": "Use 发 for sending digital messages or documents: 发微信, 发邮件.",
        "examples": ["我给你发邮件。— I send you an email.", "她发微信给我。— She sends me a WeChat message."],
        "hint": "发 sends something outward.",
    },
    {
        "hanzi": "收",
        "pinyin": "shōu",
        "english": "to receive; collect",
        "category": "Communication",
        "part": "verb",
        "usage": "Opposite of 发. Use 收邮件 for receiving email, and 收到 for successfully receiving something.",
        "examples": ["我收到你的邮件了。— I received your email.", "老师收作业。— The teacher collects homework."],
        "hint": "发 sends out; 收 pulls in.",
    },
    {
        "hanzi": "借",
        "pinyin": "jiè",
        "english": "to borrow; lend",
        "category": "Daily life",
        "part": "verb",
        "usage": "借 can mean borrow or lend depending on direction. 借给 means lend to; 跟/向...借 means borrow from.",
        "examples": ["我跟他借书。— I borrow a book from him.", "我借给你一本书。— I lend you a book."],
        "hint": "Watch the direction: borrow from vs. lend to.",
    },
    {
        "hanzi": "看",
        "pinyin": "kàn",
        "english": "to watch; look at; read",
        "category": "Media",
        "part": "verb",
        "usage": "Use 看 for visual activities: 看电影, 看电视, 看书.",
        "examples": ["我看电影。— I watch a movie.", "你看书吗？— Do you read books?"],
        "hint": "看 is for eyes: watching, seeing, reading.",
    },
    {
        "hanzi": "听",
        "pinyin": "tīng",
        "english": "to listen",
        "category": "Media",
        "part": "verb",
        "usage": "Use 听 for audio: 听音乐, 听录音, 听老师.",
        "examples": ["我听音乐。— I listen to music.", "请听录音。— Please listen to the recording."],
        "hint": "听 is for ears.",
    },
    {
        "hanzi": "复习",
        "pinyin": "fùxí",
        "english": "to review",
        "category": "Study",
        "part": "verb",
        "usage": "Use 复习 when reviewing things already learned: lessons, vocabulary, grammar, characters.",
        "examples": ["我复习生词。— I review new vocabulary.", "考试以前要复习。— Before the exam, you need to review."],
        "hint": "复 = again; 习 = study/practice.",
    },
    {
        "hanzi": "预习",
        "pinyin": "yùxí",
        "english": "to preview; prepare before class",
        "category": "Study",
        "part": "verb",
        "usage": "Use 预习 before learning something formally in class. Often used with 课文 or 生词.",
        "examples": ["我预习课文。— I preview the text.", "上课以前要预习。— Before class, you need to preview."],
        "hint": "预 = beforehand; 习 = study.",
    },
    {
        "hanzi": "坐",
        "pinyin": "zuò",
        "english": "to sit; take transportation",
        "category": "Transportation",
        "part": "verb",
        "usage": "Use 坐 for riding as a passenger: 坐飞机, 坐火车, 坐车.",
        "examples": ["我坐飞机去北京。— I take a plane to Beijing.", "他坐火车。— He takes the train."],
        "hint": "You sit inside the vehicle.",
    },
    {
        "hanzi": "骑",
        "pinyin": "qí",
        "english": "to ride",
        "category": "Transportation",
        "part": "verb",
        "usage": "Use 骑 for bikes, motorcycles, horses, and things you ride on directly.",
        "examples": ["我骑自行车。— I ride a bike.", "他骑车去学校。— He bikes to school."],
        "hint": "骑 means riding on top of something.",
    },
    {
        "hanzi": "做",
        "pinyin": "zuò",
        "english": "to do; make",
        "category": "Daily life",
        "part": "verb",
        "usage": "Use 做 for doing activities or making things. 做练习 means do exercises/practice problems.",
        "examples": ["我做练习。— I do practice exercises.", "你做什么？— What are you doing?"],
        "hint": "做 is the general do/make verb.",
    },
    {
        "hanzi": "练习",
        "pinyin": "liànxí",
        "english": "to practice; exercise",
        "category": "Study",
        "part": "verb / noun",
        "usage": "As a verb, 练习 means to practice. As a noun, it means exercise or practice problem.",
        "examples": ["我练习口语。— I practice speaking.", "这些练习很有用。— These exercises are useful."],
        "hint": "It can be both the action and the practice item.",
    },
    {
        "hanzi": "教",
        "pinyin": "jiāo",
        "english": "to teach",
        "category": "School",
        "part": "verb",
        "usage": "Use 教 with a person or subject: 教我中文, 教汉语, 教体育课.",
        "examples": ["老师教汉语。— The teacher teaches Chinese.", "你可以教我吗？— Can you teach me?"],
        "hint": "教 is the teacher action.",
    },
    {
        "hanzi": "当",
        "pinyin": "dāng",
        "english": "to serve as; work as; be",
        "category": "Roles",
        "part": "verb",
        "usage": "Use 当 for taking on a role: 当老师, 当翻译, 当学生.",
        "examples": ["我想当翻译。— I want to be a translator.", "他当老师。— He works as a teacher."],
        "hint": "当 introduces a role or job.",
    },
    {
        "hanzi": "浇",
        "pinyin": "jiāo",
        "english": "to water; pour liquid on",
        "category": "Daily life",
        "part": "verb",
        "usage": "Use 浇 with plants or flowers. 浇花 means to water flowers/plants.",
        "examples": ["我浇花。— I water the flowers.", "别忘了浇花。— Don't forget to water the plants."],
        "hint": "The 氵 radical suggests water.",
    },
    {
        "hanzi": "准备",
        "pinyin": "zhǔnbèi",
        "english": "to prepare; get ready",
        "category": "Daily life",
        "part": "verb",
        "usage": "Use 准备 before nouns or verb phrases: 准备早饭, 准备考试, 准备去学校.",
        "examples": ["我准备早饭。— I prepare breakfast.", "你准备好了吗？— Are you ready?"],
        "hint": "Prepare before doing something.",
    },
    {
        "hanzi": "买",
        "pinyin": "mǎi",
        "english": "to buy",
        "category": "Shopping",
        "part": "verb",
        "usage": "Use 买 with objects you purchase: 买东西, 买羽绒服. Be careful: 买 mǎi means buy, 卖 mài means sell.",
        "examples": ["我买东西。— I buy things.", "她买羽绒服。— She buys a down jacket."],
        "hint": "买 mǎi = buy; 卖 mài = sell.",
    },
    {
        "hanzi": "爬",
        "pinyin": "pá",
        "english": "to climb; crawl",
        "category": "Sports / nature",
        "part": "verb",
        "usage": "Use 爬 for climbing mountains/stairs or crawling. 爬山 means go hiking/mountain climbing.",
        "examples": ["我喜欢爬山。— I like hiking.", "小孩儿会爬了。— The child can crawl now."],
        "hint": "爬 often uses hands/feet to move upward.",
    },
    {
        "hanzi": "举行",
        "pinyin": "jǔxíng",
        "english": "to hold; conduct an event",
        "category": "Events",
        "part": "verb",
        "usage": "Use 举行 for organized events like parties, ceremonies, meetings, and competitions.",
        "examples": ["我们举行生日晚会。— We hold a birthday party.", "学校举行比赛。— The school holds a competition."],
        "hint": "Formal event verb: hold/conduct.",
    },
    {
        "hanzi": "参加",
        "pinyin": "cānjiā",
        "english": "to participate in; attend",
        "category": "Events",
        "part": "verb",
        "usage": "Use 参加 when joining activities/events: 参加晚会, 参加比赛, 参加会议.",
        "examples": ["我参加生日晚会。— I attend the birthday party.", "你参加比赛吗？— Are you participating in the competition?"],
        "hint": "You personally join the activity.",
    },
    {
        "hanzi": "参观",
        "pinyin": "cānguān",
        "english": "to visit/tour a place",
        "category": "Travel / places",
        "part": "verb",
        "usage": "Use 参观 for visiting places in an observational/tour sense: museums, companies, schools.",
        "examples": ["我们参观博物馆。— We tour the museum.", "他们参观公司。— They visit the company."],
        "hint": "参观 = visit and observe.",
    },
    {
        "hanzi": "锻炼",
        "pinyin": "duànliàn",
        "english": "to exercise; work out",
        "category": "Health",
        "part": "verb",
        "usage": "Use 锻炼 for physical exercise or training the body. 锻炼身体 is very common.",
        "examples": ["我每天锻炼。— I exercise every day.", "锻炼身体很重要。— Exercising is important."],
        "hint": "Think gym/workout.",
    },
    {
        "hanzi": "带",
        "pinyin": "dài",
        "english": "to bring; take along; carry",
        "category": "Daily life",
        "part": "verb",
        "usage": "Use 带 when carrying or bringing something with you: 带书, 带午饭.",
        "examples": ["我带书。— I bring books.", "你带午饭了吗？— Did you bring lunch?"],
        "hint": "带 = have something with you.",
    },
    {
        "hanzi": "玩",
        "pinyin": "wán",
        "english": "to play; have fun",
        "category": "Entertainment",
        "part": "verb",
        "usage": "Use 玩 with games, computers, or general fun activities: 玩游戏, 玩电脑.",
        "examples": ["我玩游戏。— I play games.", "他喜欢玩电脑。— He likes playing on the computer."],
        "hint": "玩 = play/fun.",
    },
    {
        "hanzi": "唱",
        "pinyin": "chàng",
        "english": "to sing",
        "category": "Entertainment",
        "part": "verb",
        "usage": "Use 唱 with songs, opera, and performances: 唱歌, 唱京剧.",
        "examples": ["我唱歌。— I sing songs.", "她会唱京剧。— She can sing Beijing opera."],
        "hint": "口 radical → singing with your mouth.",
    },
    {
        "hanzi": "学",
        "pinyin": "xué",
        "english": "to study; learn",
        "category": "Study",
        "part": "verb",
        "usage": "Use 学 with subjects or skills: 学汉语, 学书法. 学 focuses on learning.",
        "examples": ["我学汉语。— I study Chinese.", "他学书法。— He studies calligraphy."],
        "hint": "学 = learn/study.",
    },
    {
        "hanzi": "画",
        "pinyin": "huà",
        "english": "to draw; painting",
        "category": "Art",
        "part": "verb / noun",
        "usage": "As a verb, 画 means draw/paint. As a noun, it can mean a painting or drawing.",
        "examples": ["我画画儿。— I draw pictures.", "这幅画很好看。— This painting is pretty."],
        "hint": "The same character can be verb or noun.",
    },
]

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background:
            radial-gradient(circle at 18% 8%, rgba(56,189,248,.22), transparent 30%),
            radial-gradient(circle at 86% 5%, rgba(250,204,21,.16), transparent 26%),
            linear-gradient(135deg, #07111f 0%, #101827 48%, #1a1b33 100%);
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1180px;
    }

    .hero {
        padding: 26px 30px;
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(255,255,255,.14), rgba(255,255,255,.055));
        border: 1px solid rgba(255,255,255,.14);
        box-shadow: 0 28px 80px rgba(0,0,0,.35);
        margin-bottom: 20px;
    }

    .title {
        font-size: clamp(34px, 6vw, 68px);
        line-height: .95;
        font-weight: 900;
        letter-spacing: -.05em;
        margin: 0;
    }

    .subtitle {
        color: rgba(255,255,255,.70);
        font-size: 17px;
        max-width: 780px;
        margin-top: 12px;
    }

    .metric-card {
        padding: 15px 18px;
        border-radius: 20px;
        background: rgba(255,255,255,.09);
        border: 1px solid rgba(255,255,255,.11);
        text-align: center;
    }

    .metric-number {
        font-size: 28px;
        font-weight: 900;
        color: #fde047;
    }

    .metric-label {
        color: rgba(255,255,255,.62);
        font-size: 12px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: .08em;
    }

    .flash-card {
        min-height: 500px;
        padding: 34px;
        border-radius: 32px;
        border: 1px solid rgba(255,255,255,.16);
        background:
            radial-gradient(circle at top left, rgba(34,197,94,.16), transparent 32%),
            radial-gradient(circle at bottom right, rgba(250,204,21,.14), transparent 28%),
            linear-gradient(135deg, rgba(255,255,255,.14), rgba(255,255,255,.06));
        box-shadow: 0 30px 90px rgba(0,0,0,.42);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .top-row {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 26px;
        flex-wrap: wrap;
    }

    .pill {
        display: inline-flex;
        padding: 8px 14px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 900;
        border: 1px solid rgba(255,255,255,.16);
        background: rgba(255,255,255,.10);
        color: rgba(255,255,255,.82);
    }

    .gold {
        color: #fde047;
        border-color: rgba(253,224,71,.42);
        background: rgba(253,224,71,.10);
    }

    .front-hanzi {
        font-size: clamp(90px, 16vw, 190px);
        font-weight: 900;
        line-height: .95;
        text-align: center;
        text-shadow: 0 20px 70px rgba(0,0,0,.42);
        margin: 26px 0;
        word-break: keep-all;
    }

    .front-english {
        font-size: clamp(42px, 6vw, 76px);
        font-weight: 900;
        line-height: 1.05;
        text-align: center;
        text-shadow: 0 16px 60px rgba(0,0,0,.38);
        margin: 42px auto;
        max-width: 860px;
    }

    .front-usage {
        font-size: clamp(24px, 3.1vw, 38px);
        font-weight: 800;
        line-height: 1.22;
        text-align: left;
        text-shadow: 0 14px 48px rgba(0,0,0,.28);
        margin: 28px auto;
        max-width: 850px;
        color: rgba(255,255,255,.96);
    }

    .mode-label {
        text-align: center;
        color: rgba(255,255,255,.48);
        font-size: 13px;
        font-weight: 900;
        letter-spacing: .12em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .prompt {
        text-align: center;
        color: rgba(255,255,255,.70);
        font-size: 16px;
        margin-top: 12px;
    }

    .answer-box {
        padding: 22px;
        border-radius: 24px;
        border: 1px solid rgba(255,255,255,.12);
        background: rgba(255,255,255,.08);
        margin-bottom: 16px;
    }

    .box-title {
        color: #fde047;
        font-size: 13px;
        font-weight: 900;
        letter-spacing: .08em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .pinyin {
        text-align: center;
        color: #fde047;
        font-size: 31px;
        font-weight: 900;
    }

    .meaning {
        text-align: center;
        font-size: 20px;
        font-weight: 800;
        margin-top: 4px;
    }

    .muted {
        color: rgba(255,255,255,.74);
        line-height: 1.55;
    }

    .example {
        background: rgba(0,0,0,.20);
        border: 1px solid rgba(255,255,255,.08);
        border-radius: 14px;
        padding: 10px 12px;
        margin: 8px 0;
        color: rgba(255,255,255,.82);
    }

    .deck-card {
        padding: 14px 16px;
        border-radius: 18px;
        background: rgba(255,255,255,.07);
        border: 1px solid rgba(255,255,255,.10);
        margin-bottom: 10px;
    }

    .deck-hanzi {
        font-size: 27px;
        font-weight: 900;
    }

    .deck-meta {
        font-size: 13px;
        color: rgba(255,255,255,.62);
    }

    div[data-testid="stButton"] > button {
        width: 100%;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,.14);
        padding: .78rem 1rem;
        font-weight: 900;
        background: rgba(255,255,255,.10);
        color: white;
    }

    div[data-testid="stButton"] > button:hover {
        border-color: rgba(253,224,71,.75);
        background: rgba(255,255,255,.16);
        color: white;
    }

    label {
        color: rgba(255,255,255,.78) !important;
        font-weight: 800 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Helper functions
# -----------------------------
def safe(text):
    """Escape text before inserting it into custom HTML."""
    return html.escape(str(text), quote=False)


def filtered_indices(category, search):
    search = search.strip().lower()
    results = []

    for i, card in enumerate(CARDS):
        searchable_text = " ".join(
            [
                card["hanzi"],
                card["pinyin"],
                card["english"],
                card["category"],
                card["part"],
                card["usage"],
                " ".join(card["examples"]),
                card["hint"],
            ]
        ).lower()

        category_ok = category == "All" or card["category"] == category
        search_ok = not search or search in searchable_text

        if category_ok and search_ok:
            results.append(i)

    return results


def initialize_state():
    defaults = {
        "known": set(),
        "again": set(),
        "revealed": False,
        "pos": 0,
        "order": list(range(len(CARDS))),
        "filter_key": None,
        "active_indices": list(range(len(CARDS))),
        "shuffle_count": 0,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def apply_filters_if_needed(category, search):
    """
    Only reset the deck order when the filters actually change.

    This is the important fix for shuffle:
    the old code recomputed the filtered list every rerun and compared it to
    the shuffled order, so it accidentally reset the deck after every shuffle.
    """
    new_key = (category, search.strip().lower())

    if st.session_state.filter_key != new_key:
        active = filtered_indices(category, search)
        st.session_state.filter_key = new_key
        st.session_state.active_indices = active
        st.session_state.order = active.copy()
        st.session_state.pos = 0
        st.session_state.revealed = False

    return st.session_state.active_indices


def current_index():
    if not st.session_state.order:
        return None

    st.session_state.pos %= len(st.session_state.order)
    return st.session_state.order[st.session_state.pos]


def next_card():
    if st.session_state.order:
        st.session_state.pos = (st.session_state.pos + 1) % len(st.session_state.order)

    st.session_state.revealed = False


def shuffle_deck():
    if len(st.session_state.order) <= 1:
        return

    old_current = current_index()
    new_order = st.session_state.order.copy()
    random.shuffle(new_order)

    # Guarantee that shuffle visibly changes the first card when possible.
    if old_current is not None and new_order[0] == old_current:
        new_order.append(new_order.pop(0))

    st.session_state.order = new_order
    st.session_state.pos = 0
    st.session_state.revealed = False
    st.session_state.shuffle_count += 1


def reset_progress():
    st.session_state.known = set()
    st.session_state.again = set()
    st.session_state.revealed = False
    st.session_state.pos = 0


initialize_state()

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <p class="title">Chinese Flashcards</p>
        <p class="subtitle">
            Practice recognizing characters without pinyin first. Reveal the answer only after
            you try the pronunciation, meaning, and usage.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Controls
# -----------------------------
categories = ["All"] + sorted({card["category"] for card in CARDS})

control_1, control_2, control_3 = st.columns([1.1, 1.1, 1.8])

with control_1:
    mode = st.selectbox(
        "Practice mode",
        ["Hanzi → meaning", "English → Hanzi", "Usage → Hanzi"],
        index=0,
    )

with control_2:
    category = st.selectbox("Category", categories, index=0)

with control_3:
    search = st.text_input("Search", placeholder="Try: 买, pinyin, school, transportation...")

active = apply_filters_if_needed(category, search)

if not st.session_state.order:
    st.warning("No cards match your filters.")
    st.stop()

# -----------------------------
# Metrics
# -----------------------------
known_count = len(st.session_state.known)
again_count = len(st.session_state.again)
progress = round(100 * known_count / len(CARDS))

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(
        f"<div class='metric-card'><div class='metric-number'>{known_count}</div><div class='metric-label'>Known</div></div>",
        unsafe_allow_html=True,
    )
with m2:
    st.markdown(
        f"<div class='metric-card'><div class='metric-number'>{again_count}</div><div class='metric-label'>Review again</div></div>",
        unsafe_allow_html=True,
    )
with m3:
    st.markdown(
        f"<div class='metric-card'><div class='metric-number'>{progress}%</div><div class='metric-label'>Progress</div></div>",
        unsafe_allow_html=True,
    )
with m4:
    st.markdown(
        f"<div class='metric-card'><div class='metric-number'>{len(active)}</div><div class='metric-label'>Active cards</div></div>",
        unsafe_allow_html=True,
    )

st.write("")

# -----------------------------
# Current card
# -----------------------------
idx = current_index()
card = CARDS[idx]

if idx in st.session_state.known:
    status = "Known"
elif idx in st.session_state.again:
    status = "Review again"
else:
    status = "New"

if mode == "Hanzi → meaning":
    front = card["hanzi"]
    front_class = "front-hanzi"
    mode_label = "Hanzi"
    prompt = "Say the pinyin, meaning, and one example sentence. Then reveal."
elif mode == "English → Hanzi":
    front = card["english"]
    front_class = "front-english"
    mode_label = "English meaning"
    prompt = "Try to remember the Chinese characters. Then reveal."
else:
    front = card["usage"]
    front_class = "front-usage"
    mode_label = "Usage clue"
    prompt = "Guess the Chinese word from the usage explanation. Then reveal."

# -----------------------------
# Main flashcard layout
# -----------------------------
left, right = st.columns([1.65, 1])

with left:
    st.markdown(
        f"""
        <div class="flash-card">
            <div>
                <div class="top-row">
                    <span class="pill gold">Card {st.session_state.pos + 1} / {len(st.session_state.order)}</span>
                    <span class="pill">{safe(card["category"])} · {safe(card["part"])} · {safe(status)}</span>
                </div>
                <div class="mode-label">{safe(mode_label)}</div>
                <div class="{front_class}">{safe(front)}</div>
            </div>
            <div class="prompt">{safe(prompt)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    b1, b2, b3, b4, b5 = st.columns(5)

    with b1:
        if st.button("Reveal"):
            st.session_state.revealed = True
            st.rerun()

    with b2:
        if st.button("I knew it"):
            st.session_state.known.add(idx)
            st.session_state.again.discard(idx)
            next_card()
            st.rerun()

    with b3:
        if st.button("Review again"):
            st.session_state.again.add(idx)
            st.session_state.known.discard(idx)
            next_card()
            st.rerun()

    with b4:
        if st.button("Next"):
            next_card()
            st.rerun()

    with b5:
        if st.button("Shuffle"):
            shuffle_deck()
            st.rerun()

with right:
    if st.session_state.revealed:
        examples_html = "".join(
            f"<div class='example'>{safe(example)}</div>" for example in card["examples"]
        )

        st.markdown(
            f"""
            <div class="answer-box">
                <div class="box-title">Answer</div>
                <div class="pinyin">{safe(card["pinyin"])}</div>
                <div class="meaning">{safe(card["hanzi"])} · {safe(card["english"])}</div>
            </div>

            <div class="answer-box">
                <div class="box-title">How to use it</div>
                <div class="muted">{safe(card["usage"])}</div>
            </div>

            <div class="answer-box">
                <div class="box-title">Examples</div>
                {examples_html}
            </div>

            <div class="answer-box">
                <div class="box-title">Memory hint</div>
                <div class="muted">{safe(card["hint"])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="answer-box">
                <div class="box-title">Hidden answer</div>
                <div class="muted">
                    Try to remember first. The pinyin, meaning, examples, and usage will appear here after you click Reveal.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------
# Extra controls
# -----------------------------
st.write("")

extra_1, extra_2, extra_3 = st.columns([1, 1, 3])

with extra_1:
    if st.button("Restart deck"):
        st.session_state.pos = 0
        st.session_state.revealed = False
        st.rerun()

with extra_2:
    if st.button("Reset progress"):
        reset_progress()
        st.rerun()

# -----------------------------
# Deck browser
# -----------------------------
with st.expander("Deck browser", expanded=True):
    cols = st.columns(3)

    for n, card_index in enumerate(st.session_state.order):
        deck_card = CARDS[card_index]
        icon = "✅" if card_index in st.session_state.known else "🔁" if card_index in st.session_state.again else "•"

        with cols[n % 3]:
            st.markdown(
                f"""
                <div class="deck-card">
                    <div class="deck-hanzi">{safe(icon)} {safe(deck_card["hanzi"])}</div>
                    <div class="deck-meta">{safe(deck_card["pinyin"])} · {safe(deck_card["english"])}</div>
                    <div class="deck-meta">{safe(deck_card["category"])} · {safe(deck_card["part"])}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.caption("Tip: Use the filters to practice only school words, transportation words, verbs, or event vocabulary.")
