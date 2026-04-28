import html
import random
import streamlit as st

# ============================================================
# Chinese Flashcards — Native Streamlit App
# Copy-paste this entire file into app.py
# ============================================================

st.set_page_config(
    page_title="Chinese Flashcards",
    page_icon="🀄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# Vocabulary deck
# ------------------------------------------------------------
# Card types:
# - verb/action cards include deeper "usage" notes.
# - noun/object cards help you memorize the related words individually.
# - antonym cards come from the 反义词 screenshot.
# ------------------------------------------------------------

CARDS = [
    # ========================================================
    # Actions / verbs from your first page
    # ========================================================
    {
        "hanzi": "上网",
        "pinyin": "shàng wǎng",
        "english": "to go online; use the internet",
        "category": "Actions",
        "part": "verb-object phrase",
        "usage": "Use 上网 when someone uses the internet in general. 网 is already the object, so you usually do not add another object after it.",
        "examples": ["我晚上上网。— I go online at night.", "你喜欢上网吗？— Do you like going online?"],
        "hint": "上 = get on; 网 = web/net → get on the web.",
        "related": ["网"],
    },
    {
        "hanzi": "上课",
        "pinyin": "shàng kè",
        "english": "to attend class; to have class",
        "category": "Actions",
        "part": "verb-object phrase",
        "usage": "Use 上课 when someone is in class or attends class. The opposite is 下课.",
        "examples": ["我九点上课。— I have class at 9.", "我们在教室上课。— We have class in the classroom."],
        "hint": "上 = start/attend; 课 = class.",
        "related": ["课", "下课"],
    },
    {
        "hanzi": "下课",
        "pinyin": "xià kè",
        "english": "class ends; to finish class",
        "category": "Actions",
        "part": "verb-object phrase",
        "usage": "Use 下课 when class is dismissed or finished.",
        "examples": ["几点下课？— What time does class end?", "下课以后我去吃饭。— After class I go eat."],
        "hint": "下 = down/off; class comes down and ends.",
        "related": ["课", "上课"],
    },
    {
        "hanzi": "查",
        "pinyin": "chá",
        "english": "to check; look up",
        "category": "Actions",
        "part": "verb",
        "usage": "Often used with information sources: 查资料 means research/check materials; 查词典 means look something up in a dictionary.",
        "examples": ["我查词典。— I look it up in the dictionary.", "他在网上查资料。— He researches information online."],
        "hint": "查 is the action of checking or searching.",
        "related": ["资料", "词典"],
    },
    {
        "hanzi": "发",
        "pinyin": "fā",
        "english": "to send; issue",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 发 for sending digital messages or documents: 发微信, 发邮件.",
        "examples": ["我给你发邮件。— I send you an email.", "她发微信给我。— She sends me a WeChat message."],
        "hint": "发 sends something outward.",
        "related": ["微信", "邮件"],
    },
    {
        "hanzi": "收",
        "pinyin": "shōu",
        "english": "to receive; collect",
        "category": "Actions",
        "part": "verb",
        "usage": "This is often the opposite direction of 发. Use 收邮件 for receiving email, and 收到 for successfully receiving something.",
        "examples": ["我收到你的邮件了。— I received your email.", "老师收作业。— The teacher collects homework."],
        "hint": "发 sends out; 收 pulls in.",
        "related": ["邮件"],
    },
    {
        "hanzi": "借",
        "pinyin": "jiè",
        "english": "to borrow; lend",
        "category": "Actions",
        "part": "verb",
        "usage": "借 can mean borrow or lend depending on direction. 借给 means lend to; 跟/向...借 means borrow from.",
        "examples": ["我跟他借书。— I borrow a book from him.", "我借给你一本书。— I lend you a book."],
        "hint": "Watch the direction: borrow from vs. lend to.",
        "related": ["书", "词典"],
    },
    {
        "hanzi": "看",
        "pinyin": "kàn",
        "english": "to watch; look at; read",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 看 for visual activities: 看电影, 看电视剧, 看书.",
        "examples": ["我看电影。— I watch a movie.", "你看电视剧吗？— Do you watch TV dramas?"],
        "hint": "看 is for eyes: watching, seeing, reading.",
        "related": ["电影", "电视剧", "京剧"],
    },
    {
        "hanzi": "听",
        "pinyin": "tīng",
        "english": "to listen",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 听 for audio: 听音乐, 听录音, 听老师说话.",
        "examples": ["我听音乐。— I listen to music.", "请听录音。— Please listen to the recording."],
        "hint": "听 is for ears.",
        "related": ["音乐", "录音"],
    },
    {
        "hanzi": "复习",
        "pinyin": "fùxí",
        "english": "to review",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 复习 when reviewing things already learned: lessons, vocabulary, grammar, characters.",
        "examples": ["我复习生词。— I review new vocabulary.", "考试以前要复习。— Before the exam, you need to review."],
        "hint": "复 = again; 习 = study/practice.",
        "related": ["课文", "生词", "汉字", "语法"],
    },
    {
        "hanzi": "预习",
        "pinyin": "yùxí",
        "english": "to preview; prepare before class",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 预习 before learning something formally in class. Often used with 课文 or 生词.",
        "examples": ["我预习课文。— I preview the text.", "上课以前要预习。— Before class, you need to preview."],
        "hint": "预 = beforehand; 习 = study.",
        "related": ["课文", "生词"],
    },
    {
        "hanzi": "坐",
        "pinyin": "zuò",
        "english": "to sit; take transportation",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 坐 for riding as a passenger: 坐飞机, 坐火车, 坐车.",
        "examples": ["我坐飞机去北京。— I take a plane to Beijing.", "他坐火车。— He takes the train."],
        "hint": "You sit inside the vehicle.",
        "related": ["飞机", "火车"],
    },
    {
        "hanzi": "骑",
        "pinyin": "qí",
        "english": "to ride",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 骑 for bikes, motorcycles, horses, and things you ride on directly.",
        "examples": ["我骑自行车。— I ride a bike.", "他骑车去学校。— He bikes to school."],
        "hint": "骑 means riding on top of something.",
        "related": ["自行车", "车"],
    },
    {
        "hanzi": "做",
        "pinyin": "zuò",
        "english": "to do; make",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 做 for doing activities or making things. 做练习 means do exercises or practice problems.",
        "examples": ["我做练习。— I do practice exercises.", "你做什么？— What are you doing?"],
        "hint": "做 is the general do/make verb.",
        "related": ["练习"],
    },
    {
        "hanzi": "练习",
        "pinyin": "liànxí",
        "english": "to practice; exercise",
        "category": "Actions",
        "part": "verb / noun",
        "usage": "As a verb, 练习 means to practice. As a noun, it means exercise or practice problem.",
        "examples": ["我练习口语。— I practice speaking.", "这些练习很有用。— These exercises are useful."],
        "hint": "It can be both the action and the practice item.",
        "related": ["口语"],
    },
    {
        "hanzi": "教",
        "pinyin": "jiāo",
        "english": "to teach",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 教 with a person or subject: 教我中文, 教汉语, 教体育课.",
        "examples": ["老师教汉语。— The teacher teaches Chinese.", "你可以教我吗？— Can you teach me?"],
        "hint": "教 is the teacher action.",
        "related": ["综合课", "听力课", "文化课", "口语课", "阅读课", "体育课"],
    },
    {
        "hanzi": "当",
        "pinyin": "dāng",
        "english": "to serve as; work as; be",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 当 for taking on a role: 当老师, 当翻译, 当学生.",
        "examples": ["我想当翻译。— I want to be a translator.", "他当老师。— He works as a teacher."],
        "hint": "当 introduces a role or job.",
        "related": ["翻译"],
    },
    {
        "hanzi": "浇",
        "pinyin": "jiāo",
        "english": "to water; pour liquid on",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 浇 with plants or flowers. 浇花 means to water flowers or plants.",
        "examples": ["我浇花。— I water the flowers.", "别忘了浇花。— Don't forget to water the plants."],
        "hint": "The 氵 radical suggests water.",
        "related": ["花"],
    },
    {
        "hanzi": "准备",
        "pinyin": "zhǔnbèi",
        "english": "to prepare; get ready",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 准备 before nouns or verb phrases: 准备早饭, 准备考试, 准备去学校.",
        "examples": ["我准备早饭。— I prepare breakfast.", "你准备好了吗？— Are you ready?"],
        "hint": "Prepare before doing something.",
        "related": ["早饭", "午饭", "晚饭"],
    },
    {
        "hanzi": "买",
        "pinyin": "mǎi",
        "english": "to buy",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 买 with objects you purchase: 买东西, 买羽绒服. Be careful: 买 mǎi means buy, 卖 mài means sell.",
        "examples": ["我买东西。— I buy things.", "她买羽绒服。— She buys a down jacket."],
        "hint": "买 mǎi = buy; 卖 mài = sell.",
        "related": ["羽绒服", "东西"],
    },
    {
        "hanzi": "爬",
        "pinyin": "pá",
        "english": "to climb; crawl",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 爬 for climbing mountains or stairs, and also for crawling. 爬山 means go hiking or mountain climbing.",
        "examples": ["我喜欢爬山。— I like hiking.", "小孩儿会爬了。— The child can crawl now."],
        "hint": "爬 often uses hands and feet to move upward.",
        "related": ["山"],
    },
    {
        "hanzi": "举行",
        "pinyin": "jǔxíng",
        "english": "to hold; conduct an event",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 举行 for organized events like parties, ceremonies, meetings, and competitions.",
        "examples": ["我们举行生日晚会。— We hold a birthday party.", "学校举行比赛。— The school holds a competition."],
        "hint": "Formal event verb: hold or conduct.",
        "related": ["生日晚会", "晚会"],
    },
    {
        "hanzi": "参加",
        "pinyin": "cānjiā",
        "english": "to participate in; attend",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 参加 when joining activities or events: 参加晚会, 参加比赛, 参加会议.",
        "examples": ["我参加生日晚会。— I attend the birthday party.", "你参加比赛吗？— Are you participating in the competition?"],
        "hint": "You personally join the activity.",
        "related": ["生日晚会", "晚会"],
    },
    {
        "hanzi": "参观",
        "pinyin": "cānguān",
        "english": "to visit or tour a place",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 参观 for visiting places in an observational or tour sense: museums, companies, schools.",
        "examples": ["我们参观博物馆。— We tour the museum.", "他们参观公司。— They visit the company."],
        "hint": "参观 = visit and observe.",
        "related": ["博物馆", "公司"],
    },
    {
        "hanzi": "锻炼",
        "pinyin": "duànliàn",
        "english": "to exercise; work out",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 锻炼 for physical exercise or training the body. 锻炼身体 is very common.",
        "examples": ["我每天锻炼。— I exercise every day.", "锻炼身体很重要。— Exercising is important."],
        "hint": "Think gym or workout.",
        "related": ["身体"],
    },
    {
        "hanzi": "带",
        "pinyin": "dài",
        "english": "to bring; take along; carry",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 带 when carrying or bringing something with you: 带书, 带午饭.",
        "examples": ["我带书。— I bring books.", "你带午饭了吗？— Did you bring lunch?"],
        "hint": "带 = have something with you.",
        "related": ["午饭", "书"],
    },
    {
        "hanzi": "玩",
        "pinyin": "wán",
        "english": "to play; have fun",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 玩 with games, computers, or general fun activities: 玩游戏, 玩电脑.",
        "examples": ["我玩游戏。— I play games.", "他喜欢玩电脑。— He likes playing on the computer."],
        "hint": "玩 = play or fun.",
        "related": ["电脑", "游戏"],
    },
    {
        "hanzi": "唱",
        "pinyin": "chàng",
        "english": "to sing",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 唱 with songs, opera, and performances: 唱歌, 唱京剧.",
        "examples": ["我唱歌。— I sing songs.", "她会唱京剧。— She can sing Beijing opera."],
        "hint": "The 口 radical reminds you it uses your mouth.",
        "related": ["歌", "京剧"],
    },
    {
        "hanzi": "学",
        "pinyin": "xué",
        "english": "to study; learn",
        "category": "Actions",
        "part": "verb",
        "usage": "Use 学 with subjects or skills: 学汉语, 学书法. 学 focuses on learning.",
        "examples": ["我学汉语。— I study Chinese.", "他学书法。— He studies calligraphy."],
        "hint": "学 = learn or study.",
        "related": ["书法", "汉语"],
    },
    {
        "hanzi": "画",
        "pinyin": "huà",
        "english": "to draw; painting",
        "category": "Actions",
        "part": "verb / noun",
        "usage": "As a verb, 画 means draw or paint. As a noun, it can mean a painting or drawing.",
        "examples": ["我画画儿。— I draw pictures.", "这幅画很好看。— This painting is pretty."],
        "hint": "The same character can be a verb or a noun.",
        "related": ["画儿"],
    },

    # ========================================================
    # Nouns / object words from your screenshots
    # ========================================================
    {
        "hanzi": "网",
        "pinyin": "wǎng",
        "english": "net; web; internet",
        "category": "Objects",
        "part": "noun",
        "usage": "网 means net or web. In everyday Chinese, it often refers to the internet in words like 上网.",
        "examples": ["我上网。— I go online.", "这个网站很好。— This website is good."],
        "hint": "网 is the web/net.",
        "related": ["上网"],
    },
    {
        "hanzi": "课",
        "pinyin": "kè",
        "english": "class; lesson",
        "category": "School objects",
        "part": "noun",
        "usage": "课 means class or lesson. It appears in 上课, 下课, 综合课, 听力课, etc.",
        "examples": ["今天有中文课。— Today there is Chinese class.", "我喜欢这门课。— I like this course."],
        "hint": "课 = class/lesson.",
        "related": ["上课", "下课"],
    },
    {
        "hanzi": "资料",
        "pinyin": "zīliào",
        "english": "materials; information; data",
        "category": "Study objects",
        "part": "noun",
        "usage": "资料 means information or reference materials. It is common with 查: 查资料.",
        "examples": ["我查资料。— I look up information.", "这些资料很有用。— These materials are useful."],
        "hint": "Think research materials.",
        "related": ["查"],
    },
    {
        "hanzi": "词典",
        "pinyin": "cídiǎn",
        "english": "dictionary",
        "category": "Study objects",
        "part": "noun",
        "usage": "词典 means dictionary. You can 查词典 or 借词典.",
        "examples": ["我查词典。— I look it up in the dictionary.", "我借一本词典。— I borrow a dictionary."],
        "hint": "词 = word; 典 = reference book.",
        "related": ["查", "借"],
    },
    {
        "hanzi": "微信",
        "pinyin": "wēixìn",
        "english": "WeChat",
        "category": "Communication objects",
        "part": "noun",
        "usage": "微信 is WeChat. It is often used with 发: 发微信.",
        "examples": ["我给你发微信。— I send you a WeChat message.", "你有微信吗？— Do you have WeChat?"],
        "hint": "微信 = WeChat.",
        "related": ["发"],
    },
    {
        "hanzi": "邮件",
        "pinyin": "yóujiàn",
        "english": "email; mail",
        "category": "Communication objects",
        "part": "noun",
        "usage": "邮件 can mean email or mail. Use 发邮件 to send email and 收邮件 to receive email.",
        "examples": ["我发邮件。— I send an email.", "我收邮件。— I receive email."],
        "hint": "Email/mail word.",
        "related": ["发", "收"],
    },
    {
        "hanzi": "书",
        "pinyin": "shū",
        "english": "book",
        "category": "Study objects",
        "part": "noun",
        "usage": "书 means book. It can be used with 看, 借, 带.",
        "examples": ["我看书。— I read a book.", "我带书。— I bring books."],
        "hint": "书 = book.",
        "related": ["看", "借", "带"],
    },
    {
        "hanzi": "电影",
        "pinyin": "diànyǐng",
        "english": "movie",
        "category": "Media objects",
        "part": "noun",
        "usage": "电影 means movie. The usual verb is 看: 看电影.",
        "examples": ["我看电影。— I watch a movie.", "这个电影很好看。— This movie is good."],
        "hint": "电 = electric; 影 = image/shadow.",
        "related": ["看"],
    },
    {
        "hanzi": "电视剧",
        "pinyin": "diànshìjù",
        "english": "TV drama; television series",
        "category": "Media objects",
        "part": "noun",
        "usage": "电视剧 means TV drama or TV series. Usually used with 看.",
        "examples": ["我看电视剧。— I watch TV dramas.", "这个电视剧很有意思。— This TV series is interesting."],
        "hint": "电视 = television; 剧 = drama.",
        "related": ["看"],
    },
    {
        "hanzi": "京剧",
        "pinyin": "jīngjù",
        "english": "Beijing opera",
        "category": "Media objects",
        "part": "noun",
        "usage": "京剧 is Beijing opera. You can 看京剧 or 唱京剧.",
        "examples": ["我看京剧。— I watch Beijing opera.", "她会唱京剧。— She can sing Beijing opera."],
        "hint": "京 = capital/Beijing; 剧 = drama/opera.",
        "related": ["看", "唱"],
    },
    {
        "hanzi": "音乐",
        "pinyin": "yīnyuè",
        "english": "music",
        "category": "Media objects",
        "part": "noun",
        "usage": "音乐 means music. The usual verb is 听: 听音乐.",
        "examples": ["我听音乐。— I listen to music.", "我喜欢中文音乐。— I like Chinese music."],
        "hint": "音 = sound; 乐 = music.",
        "related": ["听"],
    },
    {
        "hanzi": "录音",
        "pinyin": "lùyīn",
        "english": "recording; audio recording",
        "category": "Media objects",
        "part": "noun",
        "usage": "录音 means audio recording. It is common in class instructions: 听录音.",
        "examples": ["请听录音。— Please listen to the recording.", "这个录音很清楚。— This recording is clear."],
        "hint": "录 = record; 音 = sound.",
        "related": ["听"],
    },
    {
        "hanzi": "课文",
        "pinyin": "kèwén",
        "english": "text; lesson text",
        "category": "School objects",
        "part": "noun",
        "usage": "课文 means the text or reading passage in a lesson. You can 预习课文 or 复习课文.",
        "examples": ["我预习课文。— I preview the lesson text.", "这篇课文不难。— This lesson text is not difficult."],
        "hint": "课 = lesson; 文 = text.",
        "related": ["预习", "复习"],
    },
    {
        "hanzi": "生词",
        "pinyin": "shēngcí",
        "english": "new words; vocabulary",
        "category": "School objects",
        "part": "noun",
        "usage": "生词 means new vocabulary words. Common with 预习 and 复习.",
        "examples": ["我复习生词。— I review new words.", "今天的生词很多。— Today there are many new words."],
        "hint": "生 = new/unfamiliar; 词 = word.",
        "related": ["复习", "预习"],
    },
    {
        "hanzi": "汉字",
        "pinyin": "hànzì",
        "english": "Chinese characters",
        "category": "School objects",
        "part": "noun",
        "usage": "汉字 means Chinese characters. It is useful when talking about writing or memorizing characters.",
        "examples": ["我复习汉字。— I review Chinese characters.", "这个汉字很难写。— This character is hard to write."],
        "hint": "汉 = Chinese; 字 = character.",
        "related": ["复习"],
    },
    {
        "hanzi": "语法",
        "pinyin": "yǔfǎ",
        "english": "grammar",
        "category": "School objects",
        "part": "noun",
        "usage": "语法 means grammar. You can 学语法 or 复习语法.",
        "examples": ["我复习语法。— I review grammar.", "中文语法很有意思。— Chinese grammar is interesting."],
        "hint": "语 = language; 法 = rules/method.",
        "related": ["复习", "学"],
    },
    {
        "hanzi": "飞机",
        "pinyin": "fēijī",
        "english": "airplane",
        "category": "Transportation objects",
        "part": "noun",
        "usage": "飞机 means airplane. Use 坐飞机 for taking a plane.",
        "examples": ["我坐飞机。— I take a plane.", "飞机很快。— Airplanes are fast."],
        "hint": "飞 = fly; 机 = machine.",
        "related": ["坐"],
    },
    {
        "hanzi": "火车",
        "pinyin": "huǒchē",
        "english": "train",
        "category": "Transportation objects",
        "part": "noun",
        "usage": "火车 means train. Use 坐火车 for taking the train.",
        "examples": ["他坐火车。— He takes the train.", "火车站在哪儿？— Where is the train station?"],
        "hint": "火 = fire; 车 = vehicle. Historically a steam train.",
        "related": ["坐"],
    },
    {
        "hanzi": "自行车",
        "pinyin": "zìxíngchē",
        "english": "bicycle",
        "category": "Transportation objects",
        "part": "noun",
        "usage": "自行车 means bicycle. Use 骑自行车 for riding a bike.",
        "examples": ["我骑自行车。— I ride a bicycle.", "这辆自行车很新。— This bicycle is new."],
        "hint": "自行 = self-moving; 车 = vehicle.",
        "related": ["骑"],
    },
    {
        "hanzi": "车",
        "pinyin": "chē",
        "english": "vehicle; car",
        "category": "Transportation objects",
        "part": "noun",
        "usage": "车 is a general word for vehicle, car, or bike depending on context.",
        "examples": ["我坐车去学校。— I go to school by vehicle/car.", "他骑车。— He rides a bike."],
        "hint": "General vehicle word.",
        "related": ["坐", "骑"],
    },
    {
        "hanzi": "口语",
        "pinyin": "kǒuyǔ",
        "english": "spoken language; oral Chinese",
        "category": "School objects",
        "part": "noun",
        "usage": "口语 means speaking/oral language. Use 练习口语 for practicing speaking.",
        "examples": ["我练习口语。— I practice speaking.", "口语课很有用。— Speaking class is useful."],
        "hint": "口 = mouth; 语 = language.",
        "related": ["练习", "口语课"],
    },
    {
        "hanzi": "综合课",
        "pinyin": "zōnghé kè",
        "english": "comprehensive class",
        "category": "Class names",
        "part": "noun phrase",
        "usage": "综合课 is a comprehensive/integrated language class. It may combine grammar, vocabulary, reading, and speaking.",
        "examples": ["我有综合课。— I have comprehensive class.", "综合课有点儿难。— Comprehensive class is a little hard."],
        "hint": "综合 = comprehensive; 课 = class.",
        "related": ["教"],
    },
    {
        "hanzi": "听力课",
        "pinyin": "tīnglì kè",
        "english": "listening class",
        "category": "Class names",
        "part": "noun phrase",
        "usage": "听力课 is a listening class.",
        "examples": ["今天有听力课。— Today there is listening class.", "我喜欢听力课。— I like listening class."],
        "hint": "听力 = listening ability.",
        "related": ["听", "教"],
    },
    {
        "hanzi": "文化课",
        "pinyin": "wénhuà kè",
        "english": "culture class",
        "category": "Class names",
        "part": "noun phrase",
        "usage": "文化课 means culture class.",
        "examples": ["我们上文化课。— We attend culture class.", "文化课很有意思。— Culture class is interesting."],
        "hint": "文化 = culture.",
        "related": ["教"],
    },
    {
        "hanzi": "口语课",
        "pinyin": "kǒuyǔ kè",
        "english": "speaking class",
        "category": "Class names",
        "part": "noun phrase",
        "usage": "口语课 means speaking/oral class.",
        "examples": ["口语课几点上？— What time is speaking class?", "老师教口语课。— The teacher teaches speaking class."],
        "hint": "口语 = spoken language.",
        "related": ["口语", "教"],
    },
    {
        "hanzi": "阅读课",
        "pinyin": "yuèdú kè",
        "english": "reading class",
        "category": "Class names",
        "part": "noun phrase",
        "usage": "阅读课 means reading class.",
        "examples": ["我有阅读课。— I have reading class.", "阅读课要看很多课文。— In reading class, we read many texts."],
        "hint": "阅读 = reading.",
        "related": ["课文", "教"],
    },
    {
        "hanzi": "体育课",
        "pinyin": "tǐyù kè",
        "english": "P.E.; physical education class",
        "category": "Class names",
        "part": "noun phrase",
        "usage": "体育课 means physical education class.",
        "examples": ["我喜欢体育课。— I like P.E. class.", "今天没有体育课。— Today there is no P.E. class."],
        "hint": "体育 = physical education/sports.",
        "related": ["锻炼", "教"],
    },
    {
        "hanzi": "翻译",
        "pinyin": "fānyì",
        "english": "translator; to translate",
        "category": "People / roles",
        "part": "noun / verb",
        "usage": "翻译 can mean translator or the action 'to translate'. In 当翻译, it means to work as a translator.",
        "examples": ["我想当翻译。— I want to be a translator.", "请你翻译这句话。— Please translate this sentence."],
        "hint": "Can be a person or an action.",
        "related": ["当"],
    },
    {
        "hanzi": "花",
        "pinyin": "huā",
        "english": "flower",
        "category": "Objects",
        "part": "noun",
        "usage": "花 means flower. With 浇, it forms 浇花, to water flowers/plants.",
        "examples": ["我浇花。— I water the flowers.", "这些花很好看。— These flowers are pretty."],
        "hint": "Flower word.",
        "related": ["浇"],
    },
    {
        "hanzi": "早饭",
        "pinyin": "zǎofàn",
        "english": "breakfast",
        "category": "Food objects",
        "part": "noun",
        "usage": "早饭 means breakfast. You can 吃早饭 or 准备早饭.",
        "examples": ["我吃早饭。— I eat breakfast.", "她准备早饭。— She prepares breakfast."],
        "hint": "早 = early; 饭 = meal.",
        "related": ["准备"],
    },
    {
        "hanzi": "午饭",
        "pinyin": "wǔfàn",
        "english": "lunch",
        "category": "Food objects",
        "part": "noun",
        "usage": "午饭 means lunch. You can 吃午饭, 准备午饭, or 带午饭.",
        "examples": ["我吃午饭。— I eat lunch.", "你带午饭了吗？— Did you bring lunch?"],
        "hint": "午 = noon; 饭 = meal.",
        "related": ["准备", "带"],
    },
    {
        "hanzi": "晚饭",
        "pinyin": "wǎnfàn",
        "english": "dinner",
        "category": "Food objects",
        "part": "noun",
        "usage": "晚饭 means dinner. You can 吃晚饭 or 准备晚饭.",
        "examples": ["我吃晚饭。— I eat dinner.", "我们准备晚饭。— We prepare dinner."],
        "hint": "晚 = evening; 饭 = meal.",
        "related": ["准备"],
    },
    {
        "hanzi": "羽绒服",
        "pinyin": "yǔróngfú",
        "english": "down jacket",
        "category": "Shopping objects",
        "part": "noun",
        "usage": "羽绒服 means down jacket. It is a common object with 买.",
        "examples": ["我买羽绒服。— I buy a down jacket.", "这件羽绒服很贵。— This down jacket is expensive."],
        "hint": "服 = clothing.",
        "related": ["买"],
    },
    {
        "hanzi": "东西",
        "pinyin": "dōngxi",
        "english": "thing; stuff",
        "category": "Shopping objects",
        "part": "noun",
        "usage": "东西 is a very common word meaning thing or stuff. 买东西 means to buy things / go shopping.",
        "examples": ["我买东西。— I buy things.", "这是什么东西？— What is this thing?"],
        "hint": "General word for stuff/things.",
        "related": ["买"],
    },
    {
        "hanzi": "山",
        "pinyin": "shān",
        "english": "mountain",
        "category": "Nature objects",
        "part": "noun",
        "usage": "山 means mountain. 爬山 means to climb a mountain or go hiking.",
        "examples": ["我喜欢爬山。— I like hiking.", "那座山很高。— That mountain is tall."],
        "hint": "山 even looks like mountain peaks.",
        "related": ["爬"],
    },
    {
        "hanzi": "生日晚会",
        "pinyin": "shēngrì wǎnhuì",
        "english": "birthday party",
        "category": "Events objects",
        "part": "noun phrase",
        "usage": "生日晚会 means birthday party. Use 举行 for holding one and 参加 for attending one.",
        "examples": ["我参加生日晚会。— I attend a birthday party.", "我们举行生日晚会。— We hold a birthday party."],
        "hint": "生日 = birthday; 晚会 = party/evening gathering.",
        "related": ["举行", "参加"],
    },
    {
        "hanzi": "晚会",
        "pinyin": "wǎnhuì",
        "english": "party; evening gathering",
        "category": "Events objects",
        "part": "noun",
        "usage": "晚会 is a party or evening event. It appears in 生日晚会.",
        "examples": ["我参加晚会。— I attend the party.", "这个晚会很热闹。— This party is lively."],
        "hint": "晚 = evening; 会 = gathering.",
        "related": ["生日晚会", "参加", "举行"],
    },
    {
        "hanzi": "博物馆",
        "pinyin": "bówùguǎn",
        "english": "museum",
        "category": "Places",
        "part": "noun",
        "usage": "博物馆 means museum. Use 参观博物馆 when you tour or visit a museum.",
        "examples": ["我们参观博物馆。— We visit/tour the museum.", "博物馆在哪儿？— Where is the museum?"],
        "hint": "馆 often means a building/place.",
        "related": ["参观"],
    },
    {
        "hanzi": "公司",
        "pinyin": "gōngsī",
        "english": "company",
        "category": "Places",
        "part": "noun",
        "usage": "公司 means company. Use 参观公司 when touring a company.",
        "examples": ["他们参观公司。— They visit the company.", "我爸爸在公司工作。— My dad works at a company."],
        "hint": "Company/workplace word.",
        "related": ["参观"],
    },
    {
        "hanzi": "身体",
        "pinyin": "shēntǐ",
        "english": "body; health",
        "category": "Health objects",
        "part": "noun",
        "usage": "身体 means body. 锻炼身体 is a very common phrase meaning to exercise the body / work out.",
        "examples": ["锻炼身体很重要。— Exercising is important.", "他的身体很好。— His health is good."],
        "hint": "身 = body; 体 = body/form.",
        "related": ["锻炼"],
    },
    {
        "hanzi": "电脑",
        "pinyin": "diànnǎo",
        "english": "computer",
        "category": "Technology objects",
        "part": "noun",
        "usage": "电脑 means computer. 玩电脑 can mean play/use the computer casually.",
        "examples": ["我玩电脑。— I play/use the computer.", "这台电脑很新。— This computer is new."],
        "hint": "电 = electric; 脑 = brain.",
        "related": ["玩"],
    },
    {
        "hanzi": "游戏",
        "pinyin": "yóuxì",
        "english": "game",
        "category": "Entertainment objects",
        "part": "noun",
        "usage": "游戏 means game. 玩游戏 means play games.",
        "examples": ["我玩游戏。— I play games.", "这个游戏很好玩。— This game is fun."],
        "hint": "Play object: 玩游戏.",
        "related": ["玩"],
    },
    {
        "hanzi": "歌",
        "pinyin": "gē",
        "english": "song",
        "category": "Entertainment objects",
        "part": "noun",
        "usage": "歌 means song. 唱歌 means to sing.",
        "examples": ["我唱歌。— I sing.", "这首歌很好听。— This song sounds good."],
        "hint": "歌 = song.",
        "related": ["唱"],
    },
    {
        "hanzi": "书法",
        "pinyin": "shūfǎ",
        "english": "calligraphy",
        "category": "Art / school objects",
        "part": "noun",
        "usage": "书法 means calligraphy. 学书法 means to study calligraphy.",
        "examples": ["我学书法。— I study calligraphy.", "他的书法很好。— His calligraphy is good."],
        "hint": "书 = writing; 法 = method.",
        "related": ["学"],
    },
    {
        "hanzi": "汉语",
        "pinyin": "hànyǔ",
        "english": "Chinese language",
        "category": "School objects",
        "part": "noun",
        "usage": "汉语 means Chinese language. 学汉语 means to study Chinese.",
        "examples": ["我学汉语。— I study Chinese.", "汉语很有意思。— Chinese is very interesting."],
        "hint": "汉 = Chinese; 语 = language.",
        "related": ["学", "教"],
    },
    {
        "hanzi": "画儿",
        "pinyin": "huàr",
        "english": "drawing; picture; painting",
        "category": "Art / school objects",
        "part": "noun",
        "usage": "画儿 means drawing/picture. 画画儿 means to draw pictures.",
        "examples": ["我画画儿。— I draw pictures.", "这张画儿很好看。— This picture is pretty."],
        "hint": "The 儿 changes the pronunciation to huàr.",
        "related": ["画"],
    },

    # ========================================================
    # Antonyms from the 反义词 screenshot
    # ========================================================
    {
        "hanzi": "大 — 小",
        "pinyin": "dà — xiǎo",
        "english": "big — small",
        "category": "Antonyms",
        "part": "adjective pair",
        "usage": "These are opposite adjectives. 大 describes something big or large; 小 describes something small.",
        "examples": ["这个房间很大，那个房间很小。— This room is big; that room is small.", "大狗和小猫。— A big dog and a small cat."],
        "hint": "Learn them as a pair: 大 ↔ 小.",
        "related": [],
    },
    {
        "hanzi": "贵 — 便宜",
        "pinyin": "guì — piányi",
        "english": "expensive — cheap",
        "category": "Antonyms",
        "part": "adjective pair",
        "usage": "Use 贵 for something expensive and 便宜 for something cheap or inexpensive, usually in shopping contexts.",
        "examples": ["这个衣服很贵。— This piece of clothing is expensive.", "那个很好看，而且很便宜。— That one looks nice and is also cheap."],
        "hint": "Shopping pair: 贵 ↔ 便宜.",
        "related": [],
    },
    {
        "hanzi": "长 — 短",
        "pinyin": "cháng — duǎn",
        "english": "long — short",
        "category": "Antonyms",
        "part": "adjective pair",
        "usage": "Use 长 for long length and 短 for short length. These often describe hair, time, distance, clothes, or objects.",
        "examples": ["她的头发很长。— Her hair is long.", "这条裙子太短了。— This skirt is too short."],
        "hint": "Length pair: 长 ↔ 短.",
        "related": [],
    },
    {
        "hanzi": "好看 — 难看",
        "pinyin": "hǎokàn — nánkàn",
        "english": "good-looking; nice-looking — ugly; unpleasant to look at",
        "category": "Antonyms",
        "part": "descriptive pair",
        "usage": "Use 好看 to say something looks nice or attractive. Use 难看 to say it looks ugly or bad.",
        "examples": ["这件衣服很好看。— These clothes look nice.", "这个颜色不太好看。— This color is not very nice-looking."],
        "hint": "好看 literally means good to look at; 难看 means hard or unpleasant to look at.",
        "related": [],
    },
    {
        "hanzi": "深 — 浅",
        "pinyin": "shēn — qiǎn",
        "english": "deep — shallow; dark color — light color",
        "category": "Antonyms",
        "part": "adjective pair",
        "usage": "深 and 浅 are opposites for depth. They can also describe dark vs. light shades of color.",
        "examples": ["这条河很深。— This river is deep.", "我喜欢浅蓝色。— I like light blue."],
        "hint": "Depth or color intensity pair: 深 ↔ 浅.",
        "related": [],
    },
    {
        "hanzi": "胖 — 瘦",
        "pinyin": "pàng — shòu",
        "english": "fat — thin",
        "category": "Antonyms",
        "part": "adjective pair",
        "usage": "Use 胖 to describe someone or something fat; use 瘦 for thin or skinny.",
        "examples": ["他有一点儿胖。— He is a little fat.", "她很瘦。— She is very thin."],
        "hint": "Body description pair: 胖 ↔ 瘦.",
        "related": [],
    },
    {
        "hanzi": "难 — 容易",
        "pinyin": "nán — róngyì",
        "english": "difficult — easy",
        "category": "Antonyms",
        "part": "adjective pair",
        "usage": "Use 难 for something difficult and 容易 for something easy.",
        "examples": ["汉字很难。— Chinese characters are difficult.", "这个问题很容易。— This question is easy."],
        "hint": "Difficulty pair: 难 ↔ 容易.",
        "related": [],
    },
    {
        "hanzi": "厚 — 薄",
        "pinyin": "hòu — báo",
        "english": "thick — thin",
        "category": "Antonyms",
        "part": "adjective pair",
        "usage": "Use 厚 for thick things such as books, clothes, walls, or slices. Use 薄 for thin things.",
        "examples": ["这本书很厚。— This book is thick.", "这件衣服太薄了。— These clothes are too thin."],
        "hint": "Thickness pair: 厚 ↔ 薄.",
        "related": [],
    },
    {
        "hanzi": "好听 — 难听",
        "pinyin": "hǎotīng — nántīng",
        "english": "pleasant to hear — unpleasant to hear",
        "category": "Antonyms",
        "part": "descriptive pair",
        "usage": "Use 好听 for something that sounds nice, especially music or a voice. Use 难听 for something unpleasant to hear.",
        "examples": ["这首歌很好听。— This song sounds nice.", "他说的话很难听。— What he said was unpleasant to hear."],
        "hint": "Audio pair: 好听 ↔ 难听.",
        "related": [],
    },
    {
        "hanzi": "好喝 — 难喝",
        "pinyin": "hǎohē — nánhē",
        "english": "tasty to drink — bad to drink",
        "category": "Antonyms",
        "part": "descriptive pair",
        "usage": "Use 好喝 for drinks that taste good. Use 难喝 for drinks that taste bad.",
        "examples": ["这个茶很好喝。— This tea is tasty.", "那杯咖啡很难喝。— That cup of coffee tastes bad."],
        "hint": "Drink-taste pair: 好喝 ↔ 难喝.",
        "related": [],
    },
    {
        "hanzi": "好吃 — 难吃",
        "pinyin": "hǎochī — nánchī",
        "english": "tasty — bad-tasting",
        "category": "Antonyms",
        "part": "descriptive pair",
        "usage": "Use 好吃 for food that tastes good and 难吃 for food that tastes bad.",
        "examples": ["这个菜很好吃。— This dish is delicious.", "学校的饭不太好吃。— The school food is not very tasty."],
        "hint": "Food-taste pair: 好吃 ↔ 难吃.",
        "related": [],
    },
    {
        "hanzi": "肥肉 — 瘦肉",
        "pinyin": "féiròu — shòuròu",
        "english": "fatty meat — lean meat",
        "category": "Antonyms",
        "part": "noun pair",
        "usage": "These are opposite food terms used when talking about meat. 肥肉 is fatty meat; 瘦肉 is lean meat.",
        "examples": ["我不太喜欢肥肉。— I do not really like fatty meat.", "他喜欢吃瘦肉。— He likes eating lean meat."],
        "hint": "Meat pair: 肥肉 ↔ 瘦肉.",
        "related": [],
    },
]


# ------------------------------------------------------------
# CSS
# ------------------------------------------------------------

st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background:
            radial-gradient(circle at 12% 7%, rgba(56,189,248,.22), transparent 30%),
            radial-gradient(circle at 92% 8%, rgba(250,204,21,.12), transparent 26%),
            linear-gradient(135deg, #06101c 0%, #0d1726 44%, #18192f 100%);
        color: white;
    }

    .block-container {
        padding-top: 1.45rem;
        padding-bottom: 2.2rem;
        max-width: 1250px;
    }

    label {
        color: rgba(255,255,255,.82) !important;
        font-weight: 850 !important;
    }

    .hero {
        padding: 25px 28px;
        border-radius: 30px;
        background:
            linear-gradient(135deg, rgba(255,255,255,.16), rgba(255,255,255,.055));
        border: 1px solid rgba(255,255,255,.13);
        box-shadow: 0 26px 80px rgba(0,0,0,.34);
        margin-bottom: 18px;
    }

    .title {
        margin: 0;
        font-size: clamp(34px, 5.8vw, 68px);
        line-height: .95;
        font-weight: 950;
        letter-spacing: -.055em;
    }

    .subtitle {
        margin-top: 12px;
        max-width: 900px;
        font-size: 16px;
        color: rgba(255,255,255,.72);
        line-height: 1.45;
    }

    .metric-card {
        padding: 13px 15px;
        border-radius: 20px;
        text-align: center;
        background: rgba(255,255,255,.08);
        border: 1px solid rgba(255,255,255,.10);
        box-shadow: inset 0 1px 0 rgba(255,255,255,.04);
    }

    .metric-number {
        font-size: 27px;
        font-weight: 950;
        color: #fde047;
    }

    .metric-label {
        font-size: 12px;
        letter-spacing: .08em;
        text-transform: uppercase;
        font-weight: 900;
        color: rgba(255,255,255,.58);
    }

    .flash-card {
        min-height: 500px;
        padding: 34px;
        border-radius: 32px;
        border: 1px solid rgba(255,255,255,.16);
        background:
            radial-gradient(circle at top left, rgba(34,197,94,.17), transparent 35%),
            radial-gradient(circle at bottom right, rgba(250,204,21,.14), transparent 30%),
            linear-gradient(135deg, rgba(255,255,255,.14), rgba(255,255,255,.055));
        box-shadow: 0 30px 90px rgba(0,0,0,.42);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .card-top {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        align-items: center;
        margin-bottom: 18px;
        flex-wrap: wrap;
    }

    .pill {
        display: inline-flex;
        align-items: center;
        padding: 8px 14px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 950;
        border: 1px solid rgba(253,224,71,.35);
        background: rgba(253,224,71,.10);
        color: #fde047;
    }

    .mode-label {
        text-align: center;
        color: rgba(255,255,255,.52);
        font-size: 13px;
        font-weight: 950;
        text-transform: uppercase;
        letter-spacing: .12em;
        margin-bottom: 10px;
    }

    .front-hanzi {
        font-size: clamp(76px, 13vw, 174px);
        font-weight: 950;
        line-height: 1;
        text-align: center;
        text-shadow: 0 20px 70px rgba(0,0,0,.42);
        margin: 30px 0;
        word-break: keep-all;
    }

    .front-english {
        font-size: clamp(34px, 4.9vw, 66px);
        font-weight: 950;
        line-height: 1.08;
        text-align: center;
        text-shadow: 0 16px 58px rgba(0,0,0,.38);
        margin: 44px auto;
        max-width: 880px;
    }

    .front-usage {
        font-size: clamp(22px, 2.5vw, 34px);
        font-weight: 850;
        line-height: 1.25;
        text-align: left;
        text-shadow: 0 14px 48px rgba(0,0,0,.28);
        margin: 26px auto;
        max-width: 880px;
        color: rgba(255,255,255,.97);
    }

    .prompt {
        text-align: center;
        color: rgba(255,255,255,.72);
        font-size: 16px;
        line-height: 1.5;
        margin-top: 10px;
    }

    .side-box {
        padding: 22px;
        border-radius: 24px;
        border: 1px solid rgba(255,255,255,.12);
        background: rgba(255,255,255,.08);
        margin-bottom: 16px;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
    }

    .box-title {
        color: #fde047;
        font-size: 13px;
        font-weight: 950;
        letter-spacing: .08em;
        text-transform: uppercase;
        margin-bottom: 9px;
    }

    .pinyin {
        text-align: center;
        color: #fde047;
        font-size: 30px;
        font-weight: 950;
    }

    .meaning {
        text-align: center;
        font-size: 20px;
        font-weight: 850;
        margin-top: 5px;
    }

    .muted {
        color: rgba(255,255,255,.74);
        line-height: 1.56;
    }

    .example {
        background: rgba(0,0,0,.18);
        border: 1px solid rgba(255,255,255,.08);
        border-radius: 14px;
        padding: 10px 12px;
        margin: 8px 0;
        color: rgba(255,255,255,.82);
        line-height: 1.45;
    }

    .meta-chip-wrap {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin-top: 10px;
    }

    .meta-chip {
        display: inline-flex;
        padding: 7px 12px;
        border-radius: 999px;
        background: rgba(255,255,255,.08);
        border: 1px solid rgba(255,255,255,.12);
        color: rgba(255,255,255,.84);
        font-size: 12px;
        font-weight: 850;
    }

    .subtle-caption {
        margin: 14px 0 8px 2px;
        color: rgba(255,255,255,.60);
        font-size: 12px;
        font-weight: 950;
        text-transform: uppercase;
        letter-spacing: .16em;
    }

    div[data-testid="stButton"] {
        width: 100%;
    }

    div[data-testid="stButton"] > button {
        width: 100%;
        min-height: 54px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,.14);
        padding: .82rem 1rem;
        font-weight: 900;
        font-size: 15px;
        letter-spacing: -.01em;
        background: linear-gradient(180deg, rgba(255,255,255,.17), rgba(255,255,255,.085));
        color: white;
        transition: transform .12s ease, border-color .12s ease, background .12s ease, box-shadow .12s ease;
        box-shadow: 0 10px 24px rgba(0,0,0,.18), inset 0 1px 0 rgba(255,255,255,.05);
    }

    div[data-testid="stButton"] > button:hover {
        transform: translateY(-1px);
        border-color: rgba(253,224,71,.75);
        background: linear-gradient(180deg, rgba(255,255,255,.23), rgba(255,255,255,.12));
        color: white;
        box-shadow: 0 14px 28px rgba(0,0,0,.22), inset 0 1px 0 rgba(255,255,255,.07);
    }

    div[data-testid="stButton"] > button[kind="primary"] {
        background: linear-gradient(180deg, #fde047, #facc15);
        border-color: rgba(253,224,71,.95);
        color: #0b1120;
        box-shadow: 0 14px 32px rgba(250,204,21,.22);
    }

    div[data-testid="stButton"] > button[kind="primary"]:hover {
        background: linear-gradient(180deg, #fef08a, #fde047);
        color: #0b1120;
        box-shadow: 0 16px 36px rgba(250,204,21,.28);
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 24px;
        border: 1px solid rgba(255,255,255,.12);
        background: linear-gradient(180deg, rgba(255,255,255,.085), rgba(255,255,255,.045));
        box-shadow: 0 18px 46px rgba(0,0,0,.16);
    }

    .deck-card {
        padding: 14px 16px;
        border-radius: 18px;
        background: rgba(255,255,255,.07);
        border: 1px solid rgba(255,255,255,.10);
        margin-bottom: 10px;
        min-height: 106px;
    }

    .deck-hanzi {
        font-size: 25px;
        font-weight: 950;
        color: white;
        line-height: 1.18;
    }

    .deck-meta {
        font-size: 13px;
        color: rgba(255,255,255,.63);
        line-height: 1.35;
    }

    .small-note {
        color: rgba(255,255,255,.62);
        font-size: 13px;
        line-height: 1.45;
    }

    @media (max-width: 900px) {
        .flash-card {
            min-height: 430px;
            padding: 24px;
        }
        .front-hanzi {
            font-size: clamp(68px, 22vw, 132px);
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def safe(text):
    return html.escape(str(text), quote=False)


def filtered_indices(category, search):
    search = search.strip().lower()
    results = []

    for i, card in enumerate(CARDS):
        combined = " ".join(
            [
                card["hanzi"],
                card["pinyin"],
                card["english"],
                card["category"],
                card["part"],
                card["usage"],
                " ".join(card["examples"]),
                card["hint"],
                " ".join(card.get("related", [])),
            ]
        ).lower()

        category_ok = category == "All" or card["category"] == category
        search_ok = not search or search in combined

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
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def apply_filters_if_needed(category, search):
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

    # Avoid the feeling that nothing happened if the same card lands first.
    if old_current is not None and len(new_order) > 1 and new_order[0] == old_current:
        new_order = new_order[1:] + new_order[:1]

    st.session_state.order = new_order
    st.session_state.pos = 0
    st.session_state.revealed = False


def reset_progress():
    st.session_state.known = set()
    st.session_state.again = set()
    st.session_state.revealed = False
    st.session_state.pos = 0


initialize_state()


# ------------------------------------------------------------
# Header
# ------------------------------------------------------------

st.markdown(
    f"""
    <div class="hero">
        <p class="title">Chinese Flashcards</p>
        <p class="subtitle">
            Memorize the characters first, then reveal pinyin, meaning, usage, examples, and related words.
            This version includes the verbs, object words, class names, event words, and antonyms from your screenshots.
        </p>
        <div class="small-note">Total cards in this deck: <b>{len(CARDS)}</b></div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# Top controls
# ------------------------------------------------------------

categories = ["All"] + sorted({card["category"] for card in CARDS})

c1, c2, c3 = st.columns([1.1, 1.1, 1.8])
with c1:
    mode = st.selectbox(
        "Practice mode",
        ["Hanzi → meaning", "English → Hanzi", "Usage → Hanzi"],
        index=0,
    )
with c2:
    category = st.selectbox("Category", categories, index=0)
with c3:
    search = st.text_input("Search", placeholder="Try: 邮件, 生日晚会, school, antonyms, expensive...")

active = apply_filters_if_needed(category, search)

if not st.session_state.order:
    st.warning("No cards match your filters.")
    st.stop()


# ------------------------------------------------------------
# Metrics
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# Current card
# ------------------------------------------------------------

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
    prompt = "Say the pinyin, meaning, and one possible example sentence. Then click Reveal."
elif mode == "English → Hanzi":
    front = card["english"]
    front_class = "front-english"
    mode_label = "English meaning"
    prompt = "Try to remember the Chinese characters before revealing the answer."
else:
    front = card["usage"]
    front_class = "front-usage"
    mode_label = "Usage clue"
    prompt = "Read the usage clue and try to guess the Chinese word or phrase."


# ------------------------------------------------------------
# Main layout
# ------------------------------------------------------------

left, right = st.columns([1.7, 1])

with left:
    st.markdown(
        f"""
        <div class="flash-card">
            <div>
                <div class="card-top">
                    <span class="pill">Card {st.session_state.pos + 1} / {len(st.session_state.order)}</span>
                </div>
                <div class="mode-label">{safe(mode_label)}</div>
                <div class="{front_class}">{safe(front)}</div>
            </div>
            <div class="prompt">{safe(prompt)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='subtle-caption'>Study actions</div>", unsafe_allow_html=True)

    with st.container(border=True):
        b1, b2, b3, b4, b5 = st.columns([1.04, 1.08, 1.20, 0.90, 0.98], gap="small")

        with b1:
            if st.button("👁 Reveal", type="primary", use_container_width=True):
                st.session_state.revealed = True
                st.rerun()

        with b2:
            if st.button("✅ I knew it", use_container_width=True):
                st.session_state.known.add(idx)
                st.session_state.again.discard(idx)
                next_card()
                st.rerun()

        with b3:
            if st.button("🔁 Review again", use_container_width=True):
                st.session_state.again.add(idx)
                st.session_state.known.discard(idx)
                next_card()
                st.rerun()

        with b4:
            if st.button("➡ Next", use_container_width=True):
                next_card()
                st.rerun()

        with b5:
            if st.button("🔀 Shuffle", use_container_width=True):
                shuffle_deck()
                st.rerun()

        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2, gap="small")

        with c1:
            if st.button("↺ Restart deck", use_container_width=True):
                st.session_state.pos = 0
                st.session_state.revealed = False
                st.rerun()

        with c2:
            if st.button("✦ Reset progress", use_container_width=True):
                reset_progress()
                st.rerun()


with right:
    if st.session_state.revealed:
        examples_html = "".join(
            f"<div class='example'>{safe(example)}</div>" for example in card["examples"]
        )

        related_words = card.get("related", [])
        related_html = (
            "".join(f"<span class='meta-chip'>{safe(word)}</span>" for word in related_words)
            if related_words
            else "<span class='meta-chip'>No related words listed</span>"
        )

        st.markdown(
            f"""
            <div class="side-box">
                <div class="box-title">Answer</div>
                <div class="pinyin">{safe(card["pinyin"])}</div>
                <div class="meaning">{safe(card["hanzi"])} · {safe(card["english"])}</div>
            </div>

            <div class="side-box">
                <div class="box-title">Word info</div>
                <div class="meta-chip-wrap">
                    <span class="meta-chip">{safe(card["category"])}</span>
                    <span class="meta-chip">{safe(card["part"])}</span>
                    <span class="meta-chip">{safe(status)}</span>
                </div>
            </div>

            <div class="side-box">
                <div class="box-title">How to use it</div>
                <div class="muted">{safe(card["usage"])}</div>
            </div>

            <div class="side-box">
                <div class="box-title">Examples</div>
                {examples_html}
            </div>

            <div class="side-box">
                <div class="box-title">Related words</div>
                <div class="meta-chip-wrap">{related_html}</div>
            </div>

            <div class="side-box">
                <div class="box-title">Memory hint</div>
                <div class="muted">{safe(card["hint"])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="side-box">
                <div class="box-title">Hidden answer</div>
                <div class="muted">
                    The pinyin, meaning, category, grammar type, usage notes, related words,
                    and examples stay hidden until you press <b>Reveal</b>.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ------------------------------------------------------------
# Deck browser
# ------------------------------------------------------------

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
                    <div class="deck-meta">{safe(deck_card["category"])}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.caption("Tip: use the Category dropdown to drill only Actions, Objects, Class names, Antonyms, etc.")
