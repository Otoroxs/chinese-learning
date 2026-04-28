import html
import random
import streamlit as st

# ============================================================
# Chinese Flashcards — Native Streamlit App
# Copy-paste this whole file into app.py
# ============================================================

st.set_page_config(
    page_title="Chinese Flashcards",
    page_icon="🀄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# Vocabulary deck
# ============================================================
CARDS = [{'hanzi': '上网',
  'pinyin': 'shàng wǎng',
  'english': 'to go online; to use the internet',
  'category': 'Technology',
  'part': 'verb-object phrase',
  'usage': 'Use 上网 for using the internet in general. Because 网 is already the object, do not add '
           'another object right after it.',
  'examples': ['我晚上上网。— I go online at night.', '你喜欢上网吗？— Do you like going online?'],
  'hint': '上 = get on; 网 = net/web → get on the web.'},
 {'hanzi': '上课',
  'pinyin': 'shàng kè',
  'english': 'to attend class; to have class',
  'category': 'School',
  'part': 'verb-object phrase',
  'usage': 'Use 上课 when someone is attending class or when class begins. The opposite is 下课.',
  'examples': ['我九点上课。— I have class at 9.', '我们在教室上课。— We have class in the classroom.'],
  'hint': '上 = start/attend; 课 = class.'},
 {'hanzi': '下课',
  'pinyin': 'xià kè',
  'english': 'class ends; to finish class',
  'category': 'School',
  'part': 'verb-object phrase',
  'usage': 'Use 下课 when class is over or students are dismissed.',
  'examples': ['几点下课？— What time does class end?', '我们下课以后去吃饭。— After class, we go eat.'],
  'hint': '下 is the opposite direction from 上课.'},
 {'hanzi': '查',
  'pinyin': 'chá',
  'english': 'to check; to look up',
  'category': 'Study',
  'part': 'verb',
  'usage': 'Common with information sources: 查资料, 查词典, 查地图. It means to search/check something.',
  'examples': ['我查词典。— I look it up in a dictionary.',
               '你查一下资料吧。— Please check the materials/info.'],
  'hint': 'Think: check/search.'},
 {'hanzi': '发',
  'pinyin': 'fā',
  'english': 'to send; to issue',
  'category': 'Communication',
  'part': 'verb',
  'usage': 'Common with messages and email: 发微信, 发邮件. It can also mean issue/distribute.',
  'examples': ['我给你发邮件。— I send you an email.', '他发微信给我。— He sends me a WeChat message.'],
  'hint': '发 sends something outward.'},
 {'hanzi': '收',
  'pinyin': 'shōu',
  'english': 'to receive; to collect',
  'category': 'Communication',
  'part': 'verb',
  'usage': 'Opposite direction from 发. Commonly used with 邮件: 收邮件.',
  'examples': ['你收到邮件了吗？— Did you receive the email?',
               '我每天收邮件。— I check/receive emails every day.'],
  'hint': '收 pulls something in.'},
 {'hanzi': '借',
  'pinyin': 'jiè',
  'english': 'to borrow; to lend',
  'category': 'Daily life',
  'part': 'verb',
  'usage': '借 changes meaning by direction. 跟/向 someone 借 means borrow from someone. 借给 someone '
           'means lend to someone.',
  'examples': ['我借一本书。— I borrow a book.', '我把书借给你。— I lend the book to you.'],
  'hint': 'Always check the direction: from someone or to someone.'},
 {'hanzi': '看',
  'pinyin': 'kàn',
  'english': 'to look at; to watch; to read',
  'category': 'Media',
  'part': 'verb',
  'usage': 'Use 看 with visual things: 看电影, 看书, 看电视, 看京剧.',
  'examples': ['我看电影。— I watch a movie.', '她喜欢看书。— She likes reading books.'],
  'hint': 'If your eyes are involved, 看 often works.'},
 {'hanzi': '听',
  'pinyin': 'tīng',
  'english': 'to listen',
  'category': 'Media',
  'part': 'verb',
  'usage': 'Use 听 with audio: 听音乐, 听录音, 听老师说话.',
  'examples': ['我听音乐。— I listen to music.', '请听录音。— Please listen to the recording.'],
  'hint': 'If your ears are involved, 听 often works.'},
 {'hanzi': '复习',
  'pinyin': 'fùxí',
  'english': 'to review',
  'category': 'Study',
  'part': 'verb',
  'usage': 'Use 复习 for reviewing material you already learned: 复习课文, 复习生词, 复习语法.',
  'examples': ['我复习课文。— I review the text.', '考试以前要复习。— Before an exam, you need to review.'],
  'hint': '复 = again; 习 = practice/study.'},
 {'hanzi': '预习',
  'pinyin': 'yùxí',
  'english': 'to preview; to prepare before class',
  'category': 'Study',
  'part': 'verb',
  'usage': 'Use 预习 for studying before class: 预习课文, 预习生词.',
  'examples': ['我预习生词。— I preview the new vocabulary.',
               "明天上课以前要预习。— Preview before tomorrow's class."],
  'hint': '预 = beforehand.'},
 {'hanzi': '坐',
  'pinyin': 'zuò',
  'english': 'to sit; to take transportation',
  'category': 'Transportation',
  'part': 'verb',
  'usage': 'Use 坐 for transportation you ride as a passenger: 坐飞机, 坐火车, 坐车.',
  'examples': ['我坐飞机去北京。— I go to Beijing by plane.', '他坐火车来。— He comes by train.'],
  'hint': 'You sit inside the vehicle.'},
 {'hanzi': '骑',
  'pinyin': 'qí',
  'english': 'to ride',
  'category': 'Transportation',
  'part': 'verb',
  'usage': 'Use 骑 for vehicles/animals you straddle, especially 骑自行车.',
  'examples': ['我骑自行车。— I ride a bicycle.', '你会骑车吗？— Can you ride a bike?'],
  'hint': '骑 often means riding on top of something.'},
 {'hanzi': '做',
  'pinyin': 'zuò',
  'english': 'to do; to make',
  'category': 'Daily life',
  'part': 'verb',
  'usage': 'Use 做 for doing activities or making things: 做练习, 做饭, 做作业.',
  'examples': ['我做练习。— I do exercises.', '妈妈做饭。— Mom cooks/makes food.'],
  'hint': '做 is a very general action verb.'},
 {'hanzi': '练习',
  'pinyin': 'liànxí',
  'english': 'to practice; exercise/practice item',
  'category': 'Study',
  'part': 'verb / noun',
  'usage': '练习 can be an action or a noun. 练习口语 means practice speaking. 做练习 means do exercises.',
  'examples': ['我练习口语。— I practice speaking.', '这些练习很有用。— These exercises are useful.'],
  'hint': 'It can be both the practice and the thing practiced.'},
 {'hanzi': '教',
  'pinyin': 'jiāo',
  'english': 'to teach',
  'category': 'School',
  'part': 'verb',
  'usage': 'Use 教 with a subject or person: 教汉语, 教体育课, 教我中文.',
  'examples': ['老师教汉语。— The teacher teaches Chinese.', '你可以教我吗？— Can you teach me?'],
  'hint': '教 is the teacher action.'},
 {'hanzi': '当',
  'pinyin': 'dāng',
  'english': 'to be; to work as; to serve as',
  'category': 'Roles',
  'part': 'verb',
  'usage': 'Use 当 for roles/jobs: 当老师, 当翻译, 当学生代表.',
  'examples': ['她想当老师。— She wants to be a teacher.', '我当翻译。— I work/serve as a translator.'],
  'hint': '当 points to a role someone takes.'},
 {'hanzi': '浇',
  'pinyin': 'jiāo',
  'english': 'to water; to pour liquid on',
  'category': 'Daily life',
  'part': 'verb',
  'usage': 'Most often used as 浇花, to water flowers.',
  'examples': ['我每天浇花。— I water flowers every day.', '请帮我浇一下花。— Please help me water the flowers.'],
  'hint': 'Same sound as 教, different character and meaning.'},
 {'hanzi': '准备',
  'pinyin': 'zhǔnbèi',
  'english': 'to prepare; to get ready',
  'category': 'Daily life',
  'part': 'verb',
  'usage': 'Use 准备 before what you are preparing: 准备早饭, 准备考试, 准备东西.',
  'examples': ['我准备早饭。— I prepare breakfast.', '你准备好了吗？— Are you ready?'],
  'hint': '准备好 = ready/prepared.'},
 {'hanzi': '买',
  'pinyin': 'mǎi',
  'english': 'to buy',
  'category': 'Shopping',
  'part': 'verb',
  'usage': '买 takes the thing purchased as an object: 买东西, 买羽绒服, 买书. It is the opposite of 卖 mài, '
           'to sell.',
  'examples': ['我买东西。— I buy things.', '她买了一件羽绒服。— She bought a down jacket.'],
  'hint': '买 mǎi = buy. 卖 mài = sell.'},
 {'hanzi': '爬',
  'pinyin': 'pá',
  'english': 'to climb; to crawl',
  'category': 'Sports / nature',
  'part': 'verb',
  'usage': 'Common with mountains: 爬山. It can also mean crawl.',
  'examples': ['我们星期六去爬山。— We go mountain climbing on Saturday.',
               '小孩子会爬了。— The child can crawl now.'],
  'hint': '爬山 = climb a mountain.'},
 {'hanzi': '举行',
  'pinyin': 'jǔxíng',
  'english': 'to hold; to conduct an event',
  'category': 'Events',
  'part': 'verb',
  'usage': 'Use 举行 for organized events: 举行生日晚会, 举行会议, 举行比赛.',
  'examples': ['我们举行生日晚会。— We hold a birthday party.', '学校举行比赛。— The school holds a competition.'],
  'hint': 'Formal event-holding verb.'},
 {'hanzi': '参加',
  'pinyin': 'cānjiā',
  'english': 'to participate in; to attend',
  'category': 'Events',
  'part': 'verb',
  'usage': 'Use 参加 for joining activities/events: 参加生日晚会, 参加比赛, 参加中文课.',
  'examples': ['我参加生日晚会。— I attend the birthday party.',
               '你参加比赛吗？— Are you participating in the competition?'],
  'hint': 'You join the event.'},
 {'hanzi': '参观',
  'pinyin': 'cānguān',
  'english': 'to visit/tour a place',
  'category': 'Travel / places',
  'part': 'verb',
  'usage': 'Use 参观 for visiting places like museums, companies, schools, factories.',
  'examples': ['我们参观博物馆。— We visit the museum.', '他们参观公司。— They tour the company.'],
  'hint': 'More formal than just 去.'},
 {'hanzi': '锻炼',
  'pinyin': 'duànliàn',
  'english': 'to exercise; to work out',
  'category': 'Health',
  'part': 'verb',
  'usage': 'Usually used with 身体: 锻炼身体.',
  'examples': ['我每天锻炼身体。— I exercise every day.', '锻炼对身体很好。— Exercise is good for the body.'],
  'hint': '锻炼身体 is a common fixed phrase.'},
 {'hanzi': '带',
  'pinyin': 'dài',
  'english': 'to bring; to take along; to carry',
  'category': 'Daily life',
  'part': 'verb',
  'usage': 'Use 带 for bringing/carrying something or someone: 带书, 带午饭, 带朋友.',
  'examples': ['请带书。— Please bring the book.', '我带午饭。— I bring lunch.'],
  'hint': '带 means something comes with you.'},
 {'hanzi': '玩',
  'pinyin': 'wán',
  'english': 'to play; to have fun',
  'category': 'Entertainment',
  'part': 'verb',
  'usage': 'Use 玩 with games, computers, places, or general fun: 玩游戏, 玩电脑.',
  'examples': ['我玩游戏。— I play games.', '他喜欢玩电脑。— He likes playing on the computer.'],
  'hint': '玩 is fun/play activity.'},
 {'hanzi': '唱',
  'pinyin': 'chàng',
  'english': 'to sing',
  'category': 'Entertainment',
  'part': 'verb',
  'usage': 'Common with 歌: 唱歌. You can also say 唱京剧 for singing Peking opera.',
  'examples': ['她唱歌很好听。— Her singing sounds good.', '他们唱京剧。— They sing Peking opera.'],
  'hint': '唱歌 = sing songs.'},
 {'hanzi': '学',
  'pinyin': 'xué',
  'english': 'to study; to learn',
  'category': 'Study',
  'part': 'verb',
  'usage': 'Use 学 with subjects/skills: 学汉语, 学书法, 学画画.',
  'examples': ['我学汉语。— I study Chinese.', '他学书法。— He studies calligraphy.'],
  'hint': '学 is the learner action.'},
 {'hanzi': '画',
  'pinyin': 'huà',
  'english': 'to draw; painting',
  'category': 'Art',
  'part': 'verb / noun',
  'usage': 'As a verb, 画 means draw/paint. As a noun, 画 means picture/painting. 画儿 is a colloquial '
           'noun form.',
  'examples': ['我画画儿。— I draw pictures.', '这张画很好看。— This painting looks nice.'],
  'hint': '画 can be the action or the picture.'},
 {'hanzi': '资料',
  'pinyin': 'zīliào',
  'english': 'materials; information',
  'category': 'Study',
  'part': 'noun',
  'usage': 'Often appears with 查: 查资料 means look up information/materials.',
  'examples': ['我查资料。— I look up information.', '这些资料很有用。— These materials are useful.'],
  'hint': '资料 is information you can consult.'},
 {'hanzi': '词典',
  'pinyin': 'cídiǎn',
  'english': 'dictionary',
  'category': 'Study',
  'part': 'noun',
  'usage': 'Often appears with 查 or 借: 查词典, 借词典.',
  'examples': ['我查词典。— I check the dictionary.', '可以借你的词典吗？— May I borrow your dictionary?'],
  'hint': '词 = word; 典 = reference/classic.'},
 {'hanzi': '微信',
  'pinyin': 'Wēixìn',
  'english': 'WeChat',
  'category': 'Communication',
  'part': 'noun',
  'usage': 'Use with 发: 发微信 means send a WeChat message.',
  'examples': ['我给你发微信。— I send you a WeChat message.', '你有微信吗？— Do you have WeChat?'],
  'hint': '微 = micro; 信 = message.'},
 {'hanzi': '邮件',
  'pinyin': 'yóujiàn',
  'english': 'email; mail',
  'category': 'Communication',
  'part': 'noun',
  'usage': 'Use with 发 and 收: 发邮件 = send email, 收邮件 = receive/check email.',
  'examples': ['我发邮件。— I send an email.', '她收邮件。— She checks/receives email.'],
  'hint': '邮 is related to mail.'},
 {'hanzi': '书',
  'pinyin': 'shū',
  'english': 'book',
  'category': 'School',
  'part': 'noun',
  'usage': 'Common with 看, 借, 买, 带: 看书, 借书, 买书, 带书.',
  'examples': ['我看书。— I read a book.', '请带书。— Please bring the book.'],
  'hint': 'One of the most common school nouns.'},
 {'hanzi': '电影',
  'pinyin': 'diànyǐng',
  'english': 'movie',
  'category': 'Media',
  'part': 'noun',
  'usage': 'Use with 看: 看电影 means watch a movie.',
  'examples': ['我看电影。— I watch a movie.', '这个电影很好看。— This movie is good-looking/good.'],
  'hint': '电 = electric; 影 = image/shadow.'},
 {'hanzi': '电视剧',
  'pinyin': 'diànshìjù',
  'english': 'TV drama; TV series',
  'category': 'Media',
  'part': 'noun',
  'usage': 'Use with 看: 看电视剧 means watch a TV show/drama.',
  'examples': ['她喜欢看电视剧。— She likes watching TV dramas.', '这个电视剧很长。— This TV series is long.'],
  'hint': '电视 = television; 剧 = drama.'},
 {'hanzi': '京剧',
  'pinyin': 'jīngjù',
  'english': 'Peking opera',
  'category': 'Culture',
  'part': 'noun',
  'usage': 'Use with 看 or 唱: 看京剧, 唱京剧.',
  'examples': ['我们看京剧。— We watch Peking opera.', '他会唱京剧。— He can sing Peking opera.'],
  'hint': '京 points to Beijing.'},
 {'hanzi': '音乐',
  'pinyin': 'yīnyuè',
  'english': 'music',
  'category': 'Media',
  'part': 'noun',
  'usage': 'Use with 听: 听音乐 means listen to music.',
  'examples': ['我听音乐。— I listen to music.', '这个音乐很好听。— This music sounds good.'],
  'hint': '音 = sound; 乐 = music/joy.'},
 {'hanzi': '录音',
  'pinyin': 'lùyīn',
  'english': 'recording; audio recording',
  'category': 'Media',
  'part': 'noun',
  'usage': 'Use with 听: 听录音 means listen to the recording.',
  'examples': ['请听录音。— Please listen to the recording.', '这个录音很清楚。— This recording is clear.'],
  'hint': '录 = record; 音 = sound.'},
 {'hanzi': '课文',
  'pinyin': 'kèwén',
  'english': 'text; lesson text',
  'category': 'School',
  'part': 'noun',
  'usage': 'Use with 复习/预习: 复习课文, 预习课文.',
  'examples': ['我复习课文。— I review the text.', '请预习课文。— Please preview the text.'],
  'hint': '课 = lesson; 文 = text.'},
 {'hanzi': '生词',
  'pinyin': 'shēngcí',
  'english': 'new words; vocabulary',
  'category': 'School',
  'part': 'noun',
  'usage': 'Use with 复习/预习: 复习生词, 预习生词.',
  'examples': ['我预习生词。— I preview new words.', '这些生词不难。— These new words are not hard.'],
  'hint': '生 can mean unfamiliar/new here.'},
 {'hanzi': '汉字',
  'pinyin': 'Hànzì',
  'english': 'Chinese character',
  'category': 'School',
  'part': 'noun',
  'usage': 'Use with 写, 学, 复习: 写汉字, 学汉字.',
  'examples': ['我学汉字。— I study Chinese characters.', '这个汉字很难写。— This character is hard to write.'],
  'hint': '汉 = Chinese; 字 = character.'},
 {'hanzi': '语法',
  'pinyin': 'yǔfǎ',
  'english': 'grammar',
  'category': 'School',
  'part': 'noun',
  'usage': 'Use with 学/复习: 学语法, 复习语法.',
  'examples': ['我复习语法。— I review grammar.', '中文语法很有意思。— Chinese grammar is interesting.'],
  'hint': '语 = language; 法 = method/rules.'},
 {'hanzi': '飞机',
  'pinyin': 'fēijī',
  'english': 'airplane',
  'category': 'Transportation',
  'part': 'noun',
  'usage': 'Use with 坐: 坐飞机 means take a plane.',
  'examples': ['我坐飞机去纽约。— I take a plane to New York.', '飞机很快。— Airplanes are fast.'],
  'hint': '飞 = fly; 机 = machine.'},
 {'hanzi': '火车',
  'pinyin': 'huǒchē',
  'english': 'train',
  'category': 'Transportation',
  'part': 'noun',
  'usage': 'Use with 坐: 坐火车 means take a train.',
  'examples': ['我坐火车。— I take the train.', '火车站在哪儿？— Where is the train station?'],
  'hint': '火 = fire; 车 = vehicle.'},
 {'hanzi': '车',
  'pinyin': 'chē',
  'english': 'vehicle; car',
  'category': 'Transportation',
  'part': 'noun',
  'usage': 'Use in 坐车 or 骑车. 自行车 means bicycle.',
  'examples': ['我坐车去学校。— I go to school by car/bus.', '你会骑车吗？— Can you ride a bike?'],
  'hint': 'A broad word for vehicles.'},
 {'hanzi': '口语',
  'pinyin': 'kǒuyǔ',
  'english': 'spoken language; speaking',
  'category': 'School',
  'part': 'noun',
  'usage': 'Use with 练习 or 课: 练习口语, 口语课.',
  'examples': ['我练习口语。— I practice speaking.', '今天有口语课。— Today there is speaking class.'],
  'hint': '口 = mouth; 语 = language.'},
 {'hanzi': '综合课',
  'pinyin': 'zōnghé kè',
  'english': 'comprehensive class',
  'category': 'Courses',
  'part': 'noun',
  'usage': 'A type of class. Use with 上: 上综合课.',
  'examples': ['我今天上综合课。— I have comprehensive class today.'],
  'hint': '课 means class.'},
 {'hanzi': '听力课',
  'pinyin': 'tīnglì kè',
  'english': 'listening class',
  'category': 'Courses',
  'part': 'noun',
  'usage': 'A class focused on listening skills. Use with 上.',
  'examples': ['明天有听力课。— Tomorrow there is listening class.'],
  'hint': '听力 = listening ability.'},
 {'hanzi': '文化课',
  'pinyin': 'wénhuà kè',
  'english': 'culture class',
  'category': 'Courses',
  'part': 'noun',
  'usage': 'A class about culture. Use with 上.',
  'examples': ['我们上文化课。— We attend culture class.'],
  'hint': '文化 = culture.'},
 {'hanzi': '口语课',
  'pinyin': 'kǒuyǔ kè',
  'english': 'speaking class',
  'category': 'Courses',
  'part': 'noun',
  'usage': 'A class focused on speaking. Use with 上.',
  'examples': ['我喜欢口语课。— I like speaking class.'],
  'hint': '口语 = spoken language.'},
 {'hanzi': '阅读课',
  'pinyin': 'yuèdú kè',
  'english': 'reading class',
  'category': 'Courses',
  'part': 'noun',
  'usage': 'A class focused on reading. Use with 上.',
  'examples': ['今天没有阅读课。— Today there is no reading class.'],
  'hint': '阅读 = reading.'},
 {'hanzi': '体育课',
  'pinyin': 'tǐyù kè',
  'english': 'P.E.; physical education class',
  'category': 'Courses',
  'part': 'noun',
  'usage': 'A sports/physical education class. Use with 上 or 教.',
  'examples': ['老师教体育课。— The teacher teaches P.E.', '我星期五上体育课。— I have P.E. on Friday.'],
  'hint': '体育 = physical education/sports.'},
 {'hanzi': '翻译',
  'pinyin': 'fānyì',
  'english': 'translation; translator; to translate',
  'category': 'Roles',
  'part': 'verb / noun',
  'usage': 'Can be a job/person or an action. 当翻译 means to work as a translator.',
  'examples': ['我当翻译。— I work as a translator.', '请翻译这个句子。— Please translate this sentence.'],
  'hint': 'Can be both person and action.'},
 {'hanzi': '花',
  'pinyin': 'huā',
  'english': 'flower',
  'category': 'Daily life',
  'part': 'noun',
  'usage': 'Common with 浇: 浇花 means water flowers.',
  'examples': ['我浇花。— I water flowers.', '这些花很好看。— These flowers are pretty.'],
  'hint': 'Think of flowers needing water.'},
 {'hanzi': '早饭',
  'pinyin': 'zǎofàn',
  'english': 'breakfast',
  'category': 'Food',
  'part': 'noun',
  'usage': 'Use with 吃 or 准备: 吃早饭, 准备早饭.',
  'examples': ['我吃早饭。— I eat breakfast.', '妈妈准备早饭。— Mom prepares breakfast.'],
  'hint': '早 = early; 饭 = meal.'},
 {'hanzi': '午饭',
  'pinyin': 'wǔfàn',
  'english': 'lunch',
  'category': 'Food',
  'part': 'noun',
  'usage': 'Use with 吃, 做, 带: 吃午饭, 做午饭, 带午饭.',
  'examples': ['我吃午饭。— I eat lunch.', '我带午饭。— I bring lunch.'],
  'hint': '午 = noon.'},
 {'hanzi': '晚饭',
  'pinyin': 'wǎnfàn',
  'english': 'dinner',
  'category': 'Food',
  'part': 'noun',
  'usage': 'Use with 吃, 做, 准备: 吃晚饭, 做晚饭.',
  'examples': ['我们吃晚饭。— We eat dinner.', '他做晚饭。— He makes dinner.'],
  'hint': '晚 = evening.'},
 {'hanzi': '羽绒服',
  'pinyin': 'yǔróngfú',
  'english': 'down jacket',
  'category': 'Shopping',
  'part': 'noun',
  'usage': 'Use with 买 or 穿: 买羽绒服, 穿羽绒服.',
  'examples': ['我买羽绒服。— I buy a down jacket.',
               '今天很冷，穿羽绒服吧。— It is cold today, wear a down jacket.'],
  'hint': '服 = clothing.'},
 {'hanzi': '东西',
  'pinyin': 'dōngxi',
  'english': 'thing; stuff',
  'category': 'Shopping',
  'part': 'noun',
  'usage': 'Very common object word. 买东西 means buy things.',
  'examples': ['我买东西。— I buy things.', '这是什么东西？— What thing is this?'],
  'hint': 'Useful when you do not name the object.'},
 {'hanzi': '山',
  'pinyin': 'shān',
  'english': 'mountain',
  'category': 'Sports / nature',
  'part': 'noun',
  'usage': 'Common in 爬山, to climb/hike a mountain.',
  'examples': ['我们爬山。— We climb/hike a mountain.', '那座山很高。— That mountain is tall.'],
  'hint': '爬山 is a fixed phrase.'},
 {'hanzi': '生日晚会',
  'pinyin': 'shēngrì wǎnhuì',
  'english': 'birthday party',
  'category': 'Events',
  'part': 'noun',
  'usage': 'Use with 举行 or 参加: 举行生日晚会, 参加生日晚会.',
  'examples': ['我参加生日晚会。— I attend a birthday party.', '他们举行生日晚会。— They hold a birthday party.'],
  'hint': '生日 = birthday; 晚会 = evening party.'},
 {'hanzi': '博物馆',
  'pinyin': 'bówùguǎn',
  'english': 'museum',
  'category': 'Travel / places',
  'part': 'noun',
  'usage': 'Use with 参观: 参观博物馆.',
  'examples': ['我们参观博物馆。— We visit the museum.', '博物馆很大。— The museum is big.'],
  'hint': '馆 often means building/place.'},
 {'hanzi': '公司',
  'pinyin': 'gōngsī',
  'english': 'company',
  'category': 'Travel / places',
  'part': 'noun',
  'usage': 'Use with 参观 or 去: 参观公司, 去公司.',
  'examples': ['他们参观公司。— They tour the company.', '我去公司。— I go to the company/office.'],
  'hint': 'A workplace/company.'},
 {'hanzi': '身体',
  'pinyin': 'shēntǐ',
  'english': 'body; health',
  'category': 'Health',
  'part': 'noun',
  'usage': 'Common with 锻炼: 锻炼身体 means exercise the body.',
  'examples': ['锻炼身体很重要。— Exercising is important.', '你的身体好吗？— Is your health/body good?'],
  'hint': '身 = body/person; 体 = body.'},
 {'hanzi': '电脑',
  'pinyin': 'diànnǎo',
  'english': 'computer',
  'category': 'Technology',
  'part': 'noun',
  'usage': 'Use with 玩, 用, 买: 玩电脑, 用电脑, 买电脑.',
  'examples': ['我用电脑。— I use a computer.', '他玩电脑。— He plays on the computer.'],
  'hint': '电 = electric; 脑 = brain.'},
 {'hanzi': '游戏',
  'pinyin': 'yóuxì',
  'english': 'game',
  'category': 'Entertainment',
  'part': 'noun',
  'usage': 'Use with 玩: 玩游戏 means play games.',
  'examples': ['我玩游戏。— I play games.', '这个游戏很有意思。— This game is interesting.'],
  'hint': '玩游戏 is a common phrase.'},
 {'hanzi': '歌',
  'pinyin': 'gē',
  'english': 'song',
  'category': 'Entertainment',
  'part': 'noun',
  'usage': 'Use with 唱 or 听: 唱歌, 听歌.',
  'examples': ['她唱歌。— She sings.', '我听歌。— I listen to songs.'],
  'hint': '唱歌 = sing.'},
 {'hanzi': '书法',
  'pinyin': 'shūfǎ',
  'english': 'calligraphy',
  'category': 'Art',
  'part': 'noun',
  'usage': 'Use with 学: 学书法.',
  'examples': ['我学书法。— I study calligraphy.', '书法很漂亮。— Calligraphy is beautiful.'],
  'hint': '书 = writing/book; 法 = method.'},
 {'hanzi': '汉语',
  'pinyin': 'Hànyǔ',
  'english': 'Chinese language',
  'category': 'School',
  'part': 'noun',
  'usage': 'Use with 学 or 教: 学汉语, 教汉语.',
  'examples': ['我学汉语。— I study Chinese.', '老师教汉语。— The teacher teaches Chinese.'],
  'hint': '语 means language.'},
 {'hanzi': '画儿',
  'pinyin': 'huàr',
  'english': 'picture; drawing',
  'category': 'Art',
  'part': 'noun',
  'usage': 'Colloquial form of 画 as a noun. Common in 画画儿.',
  'examples': ['我画画儿。— I draw pictures.', '这张画儿很好看。— This picture is pretty.'],
  'hint': 'The 儿 makes it sound more colloquial/northern.'},
 {'hanzi': '大',
  'pinyin': 'dà',
  'english': 'big',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 小. Use before nouns or after 很: 大房子, 很大.',
  'examples': ['这个学校很大。— This school is big.', '大苹果。— Big apple.'],
  'hint': 'Opposite pair: 大 — 小.'},
 {'hanzi': '小',
  'pinyin': 'xiǎo',
  'english': 'small',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 大. Use before nouns or after 很: 小房子, 很小.',
  'examples': ['我的房间很小。— My room is small.', '小猫。— Small cat.'],
  'hint': 'Opposite pair: 大 — 小.'},
 {'hanzi': '贵',
  'pinyin': 'guì',
  'english': 'expensive',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 便宜. Use for prices: 很贵, 不贵.',
  'examples': ['这个电脑很贵。— This computer is expensive.', '羽绒服贵不贵？— Is the down jacket expensive?'],
  'hint': 'Opposite pair: 贵 — 便宜.'},
 {'hanzi': '便宜',
  'pinyin': 'piányi',
  'english': 'cheap; inexpensive',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 贵. Useful when shopping.',
  'examples': ['这个东西很便宜。— This thing is cheap.', '那件衣服不便宜。— That clothing item is not cheap.'],
  'hint': 'Opposite pair: 贵 — 便宜.'},
 {'hanzi': '长',
  'pinyin': 'cháng',
  'english': 'long',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 短. Use for length or time duration.',
  'examples': ['这节课很长。— This class is long.', '她的头发很长。— Her hair is long.'],
  'hint': 'Opposite pair: 长 — 短.'},
 {'hanzi': '短',
  'pinyin': 'duǎn',
  'english': 'short',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 长. Use for length or time duration.',
  'examples': ['这个电影很短。— This movie is short.', '我的头发短。— My hair is short.'],
  'hint': 'Opposite pair: 长 — 短.'},
 {'hanzi': '好看',
  'pinyin': 'hǎokàn',
  'english': 'good-looking; nice to watch/read',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Use 好看 for visual appeal: people, clothes, movies, characters, books.',
  'examples': ['这个电影很好看。— This movie is good.', '这件衣服很好看。— This clothing looks nice.'],
  'hint': 'Opposite pair: 好看 — 难看.'},
 {'hanzi': '难看',
  'pinyin': 'nánkàn',
  'english': 'ugly; bad-looking',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 好看. It can be strong/rude when describing people.',
  'examples': ['这个颜色有点儿难看。— This color is a bit ugly.',
               '这张照片不好看。— This photo is not good-looking.'],
  'hint': 'Opposite pair: 好看 — 难看.'},
 {'hanzi': '深',
  'pinyin': 'shēn',
  'english': 'deep; dark/intense',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 浅. Can describe depth or color intensity.',
  'examples': ['这个水很深。— This water is deep.', '深蓝色。— Dark blue.'],
  'hint': 'Opposite pair: 深 — 浅.'},
 {'hanzi': '浅',
  'pinyin': 'qiǎn',
  'english': 'shallow; light/pale',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 深. Can describe water depth or color lightness.',
  'examples': ['这里水很浅。— The water here is shallow.', '浅蓝色。— Light blue.'],
  'hint': 'Opposite pair: 深 — 浅.'},
 {'hanzi': '胖',
  'pinyin': 'pàng',
  'english': 'fat; plump',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 瘦. Be careful using it directly with people because it can sound rude.',
  'examples': ['这只猫很胖。— This cat is fat/plump.', '他不胖。— He is not fat.'],
  'hint': 'Opposite pair: 胖 — 瘦.'},
 {'hanzi': '瘦',
  'pinyin': 'shòu',
  'english': 'thin; skinny',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 胖. Can describe people, animals, or meat.',
  'examples': ['她很瘦。— She is thin.', '瘦肉。— Lean meat.'],
  'hint': 'Opposite pair: 胖 — 瘦.'},
 {'hanzi': '难',
  'pinyin': 'nán',
  'english': 'difficult',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 容易. Use for tasks, classes, questions, characters.',
  'examples': ['中文难吗？— Is Chinese difficult?', '这个汉字很难。— This character is difficult.'],
  'hint': 'Opposite pair: 难 — 容易.'},
 {'hanzi': '容易',
  'pinyin': 'róngyì',
  'english': 'easy',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 难. Use for tasks, questions, grammar, characters.',
  'examples': ['这个问题很容易。— This question is easy.', '汉语不容易。— Chinese is not easy.'],
  'hint': 'Opposite pair: 难 — 容易.'},
 {'hanzi': '厚',
  'pinyin': 'hòu',
  'english': 'thick',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 薄. Use for books, clothes, materials, meat slices.',
  'examples': ['这本书很厚。— This book is thick.', '厚衣服。— Thick clothes.'],
  'hint': 'Opposite pair: 厚 — 薄.'},
 {'hanzi': '薄',
  'pinyin': 'báo',
  'english': 'thin',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 厚. Use for physical thinness of objects/materials.',
  'examples': ['这张纸很薄。— This paper is thin.', '薄衣服。— Thin clothes.'],
  'hint': 'Opposite pair: 厚 — 薄.'},
 {'hanzi': '好听',
  'pinyin': 'hǎotīng',
  'english': 'pleasant to hear; sounds good',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Use 好听 for sounds, voices, songs, music.',
  'examples': ['这首歌很好听。— This song sounds good.', '她唱歌很好听。— Her singing sounds good.'],
  'hint': '听 means listen → sound quality.'},
 {'hanzi': '难听',
  'pinyin': 'nántīng',
  'english': 'unpleasant to hear; sounds bad',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 好听. Use for unpleasant sounds, voices, songs, or rude words.',
  'examples': ['这个声音很难听。— This sound is unpleasant.', '他说的话很难听。— What he said sounded harsh/rude.'],
  'hint': 'Opposite pair: 好听 — 难听.'},
 {'hanzi': '好喝',
  'pinyin': 'hǎohē',
  'english': 'tasty to drink',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Use 好喝 only for drinks/liquids.',
  'examples': ['这个茶很好喝。— This tea tastes good.', '咖啡好喝吗？— Does the coffee taste good?'],
  'hint': '喝 means drink → drink quality.'},
 {'hanzi': '难喝',
  'pinyin': 'nánhē',
  'english': 'bad-tasting to drink',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 好喝. Use only for drinks/liquids.',
  'examples': ['这个药很难喝。— This medicine tastes bad.', '这杯咖啡不好喝。— This coffee does not taste good.'],
  'hint': 'Opposite pair: 好喝 — 难喝.'},
 {'hanzi': '好吃',
  'pinyin': 'hǎochī',
  'english': 'tasty to eat',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Use 好吃 only for food.',
  'examples': ['这个菜很好吃。— This dish is delicious.', '晚饭好吃吗？— Is dinner tasty?'],
  'hint': '吃 means eat → food quality.'},
 {'hanzi': '难吃',
  'pinyin': 'nánchī',
  'english': 'bad-tasting to eat',
  'category': 'Antonyms',
  'part': 'adjective',
  'usage': 'Opposite of 好吃. Use only for food.',
  'examples': ['这个菜很难吃。— This dish tastes bad.', '学校的午饭不难吃。— The school lunch is not bad.'],
  'hint': 'Opposite pair: 好吃 — 难吃.'},
 {'hanzi': '肥肉',
  'pinyin': 'féiròu',
  'english': 'fatty meat',
  'category': 'Food',
  'part': 'noun',
  'usage': 'Opposite of 瘦肉. 肥 here means fatty, not just fat as a body adjective.',
  'examples': ['我不喜欢肥肉。— I do not like fatty meat.', '肥肉太油了。— Fatty meat is too oily.'],
  'hint': 'Opposite pair: 肥肉 — 瘦肉.'},
 {'hanzi': '瘦肉',
  'pinyin': 'shòuròu',
  'english': 'lean meat',
  'category': 'Food',
  'part': 'noun',
  'usage': 'Opposite of 肥肉. 瘦肉 means meat without much fat.',
  'examples': ['我喜欢瘦肉。— I like lean meat.', '请买一点儿瘦肉。— Please buy a little lean meat.'],
  'hint': 'Opposite pair: 肥肉 — 瘦肉.'}]

# Fast, precomputed search/category helpers.
SEARCH_TEXT = [
    " ".join(
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
    for card in CARDS
]
CATEGORIES = ["All"] + sorted({card["category"] for card in CARDS})

# ============================================================
# CSS — no iframe/components, only native Streamlit + CSS
# ============================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@500;700;900&family=Inter:wght@500;700;900&display=swap');

    :root {
        --bg-a:#061525;
        --bg-b:#15182f;
        --panel:rgba(255,255,255,.075);
        --panel-strong:rgba(255,255,255,.115);
        --border:rgba(255,255,255,.15);
        --text:rgba(255,255,255,.94);
        --muted:rgba(255,255,255,.68);
        --yellow:#fde047;
        --green:#22c55e;
        --red:#fb7185;
        --blue:#38bdf8;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(circle at 12% 7%, rgba(56,189,248,.27), transparent 34%),
            radial-gradient(circle at 84% 15%, rgba(250,204,21,.13), transparent 27%),
            linear-gradient(135deg, var(--bg-a), var(--bg-b));
        color: var(--text);
        font-family: Inter, "Noto Sans SC", sans-serif;
    }

    [data-testid="stHeader"] { background: transparent; }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        border:1px solid var(--border);
        border-radius:30px;
        padding:24px 28px;
        background:linear-gradient(135deg, rgba(255,255,255,.105), rgba(255,255,255,.045));
        box-shadow:0 22px 70px rgba(0,0,0,.25);
        margin-bottom:18px;
    }
    .title {
        margin:0;
        font-size:34px;
        line-height:1.05;
        font-weight:950;
        letter-spacing:-.045em;
    }
    .subtitle {
        margin:10px 0 0 0;
        color:var(--muted);
        font-size:15px;
        max-width:800px;
        line-height:1.5;
    }

    .metric-card {
        border:1px solid var(--border);
        border-radius:20px;
        padding:15px 17px;
        background:rgba(255,255,255,.07);
        box-shadow:0 14px 36px rgba(0,0,0,.14);
    }
    .metric-value { font-size:24px; font-weight:950; line-height:1; }
    .metric-label {
        color:var(--muted);
        margin-top:6px;
        font-size:12px;
        text-transform:uppercase;
        letter-spacing:.12em;
        font-weight:900;
    }

    .study-card {
        min-height:445px;
        border-radius:30px;
        border:1px solid rgba(255,255,255,.16);
        background:
            radial-gradient(circle at 18% 10%, rgba(45,212,191,.20), transparent 36%),
            radial-gradient(circle at 85% 88%, rgba(253,224,71,.12), transparent 30%),
            linear-gradient(135deg, rgba(255,255,255,.12), rgba(255,255,255,.055));
        box-shadow:0 26px 80px rgba(0,0,0,.30);
        padding:32px;
        display:flex;
        flex-direction:column;
        justify-content:space-between;
        overflow:hidden;
    }
    .card-top {
        display:flex;
        justify-content:space-between;
        align-items:flex-start;
        gap:14px;
    }
    .pill {
        display:inline-flex;
        align-items:center;
        border:1px solid rgba(253,224,71,.68);
        color:var(--yellow);
        border-radius:999px;
        padding:9px 14px;
        font-size:13px;
        font-weight:950;
        white-space:nowrap;
    }
    .mode-label {
        color:rgba(255,255,255,.58);
        text-transform:uppercase;
        letter-spacing:.14em;
        font-size:12px;
        font-weight:950;
        text-align:center;
        margin-bottom:20px;
    }
    .prompt {
        text-align:center;
        font-weight:950;
        color:white;
        text-shadow:0 12px 32px rgba(0,0,0,.30);
        word-break:normal;
        overflow-wrap:break-word;
        max-width:100%;
        margin:0 auto;
    }
    .prompt-hanzi {
        font-family:"Noto Sans SC", Inter, sans-serif;
        font-size:clamp(58px, 9vw, 126px);
        line-height:1.05;
        letter-spacing:-.035em;
    }
    .prompt-english {
        font-size:clamp(34px, 5.5vw, 70px);
        line-height:1.08;
        letter-spacing:-.04em;
        max-width:780px;
    }
    .prompt-usage {
        font-size:clamp(26px, 3.7vw, 46px);
        line-height:1.14;
        letter-spacing:-.025em;
        max-width:820px;
    }
    .instruction {
        text-align:center;
        color:rgba(255,255,255,.78);
        font-weight:750;
        font-size:15px;
        line-height:1.45;
    }

    .answer-box {
        border:1px solid var(--border);
        border-radius:24px;
        background:rgba(255,255,255,.075);
        padding:20px;
        margin-bottom:14px;
        box-shadow:0 18px 42px rgba(0,0,0,.14);
    }
    .box-title {
        color:var(--yellow);
        font-size:12px;
        text-transform:uppercase;
        letter-spacing:.16em;
        font-weight:950;
        margin-bottom:10px;
    }
    .pinyin { color:rgba(255,255,255,.90); font-size:22px; font-weight:950; }
    .meaning { font-size:17px; color:rgba(255,255,255,.88); font-weight:850; }
    .muted { color:rgba(255,255,255,.72); font-size:15px; line-height:1.55; }
    .example {
        border-left:3px solid rgba(253,224,71,.78);
        padding-left:12px;
        margin:10px 0;
        color:rgba(255,255,255,.86);
        line-height:1.45;
    }

    .caption-label {
        margin:16px 0 8px 2px;
        color:rgba(255,255,255,.64);
        font-size:12px;
        font-weight:950;
        text-transform:uppercase;
        letter-spacing:.16em;
    }

    .action-shell {
        border:1px solid rgba(255,255,255,.13);
        border-radius:24px;
        background:linear-gradient(180deg, rgba(255,255,255,.085), rgba(255,255,255,.045));
        box-shadow:0 18px 46px rgba(0,0,0,.17);
        padding:14px;
        margin-top:4px;
    }

    .deck-card {
        border:1px solid rgba(255,255,255,.10);
        border-radius:18px;
        padding:13px 14px;
        margin-bottom:10px;
        background:rgba(255,255,255,.055);
    }
    .deck-hanzi {
        font-family:"Noto Sans SC", Inter, sans-serif;
        font-size:25px;
        font-weight:950;
    }
    .deck-meta { font-size:12px; color:rgba(255,255,255,.65); line-height:1.35; }

    div[data-testid="stButton"] { width:100%; }
    div[data-testid="stButton"] > button {
        width:100%;
        min-height:50px;
        border-radius:16px;
        border:1px solid rgba(255,255,255,.15);
        padding:.78rem .9rem;
        font-weight:900;
        font-size:14.5px;
        letter-spacing:-.01em;
        background:linear-gradient(180deg, rgba(255,255,255,.17), rgba(255,255,255,.085));
        color:white;
        transition:transform .12s ease, border-color .12s ease, background .12s ease, box-shadow .12s ease;
        box-shadow:0 10px 24px rgba(0,0,0,.18), inset 0 1px 0 rgba(255,255,255,.05);
    }
    div[data-testid="stButton"] > button:hover {
        transform:translateY(-1px);
        border-color:rgba(253,224,71,.70);
        background:linear-gradient(180deg, rgba(255,255,255,.23), rgba(255,255,255,.12));
        color:white;
        box-shadow:0 14px 28px rgba(0,0,0,.22), inset 0 1px 0 rgba(255,255,255,.07);
    }
    div[data-testid="stButton"] > button[kind="primary"] {
        background:linear-gradient(180deg, #fde047, #facc15);
        border-color:rgba(253,224,71,.95);
        color:#0b1120;
        box-shadow:0 14px 32px rgba(250,204,21,.24);
    }
    div[data-testid="stButton"] > button[kind="primary"]:hover {
        background:linear-gradient(180deg, #fef08a, #fde047);
        color:#0b1120;
        box-shadow:0 16px 36px rgba(250,204,21,.30);
    }

    label { color:rgba(255,255,255,.88) !important; font-weight:800 !important; }
    input, textarea, [data-baseweb="select"] { border-radius:16px !important; }
    .stExpander { border-radius:22px !important; }

    @media (max-width: 900px) {
        .study-card { min-height:380px; padding:24px; }
        .prompt-hanzi { font-size:clamp(54px, 18vw, 96px); }
        .prompt-english { font-size:clamp(32px, 12vw, 56px); }
        .prompt-usage { font-size:clamp(24px, 8vw, 38px); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Session state
# ============================================================
if "known" not in st.session_state:
    st.session_state.known = set()
if "again" not in st.session_state:
    st.session_state.again = set()
if "revealed" not in st.session_state:
    st.session_state.revealed = False
if "order" not in st.session_state:
    st.session_state.order = list(range(len(CARDS)))
if "pos" not in st.session_state:
    st.session_state.pos = 0
if "filter_key" not in st.session_state:
    st.session_state.filter_key = None

# In case Streamlit ever serializes sets differently.
st.session_state.known = set(st.session_state.known)
st.session_state.again = set(st.session_state.again)

# ============================================================
# Helpers
# ============================================================
def e(value: object) -> str:
    """Escape text before placing it in custom HTML."""
    return html.escape(str(value), quote=True)


def matches_filter(i: int, category: str, search: str) -> bool:
    category_ok = category == "All" or CARDS[i]["category"] == category
    search_ok = not search or search.lower() in SEARCH_TEXT[i]
    return category_ok and search_ok


def active_indices(category: str, search: str) -> list[int]:
    """Cards matching the filter that are not known."""
    search = search.strip().lower()
    return [
        i
        for i in range(len(CARDS))
        if i not in st.session_state.known and matches_filter(i, category, search)
    ]


def browser_indices(category: str, search: str, include_known: bool) -> list[int]:
    search = search.strip().lower()
    result = []
    for i in range(len(CARDS)):
        if not include_known and i in st.session_state.known:
            continue
        if matches_filter(i, category, search):
            result.append(i)
    return result


def set_order(indices: list[int]) -> None:
    st.session_state.order = list(indices)
    st.session_state.pos = 0
    st.session_state.revealed = False


def sync_order(category: str, search: str) -> None:
    """
    Keep the deck stable across reruns, but remove known cards immediately.
    This prevents the old bug where I knew it could still show that card again.
    """
    search_key = search.strip().lower()
    key = (category, search_key)
    active = active_indices(category, search_key)
    active_set = set(active)

    # If the user changed filters, rebuild the order for the new filtered deck.
    if st.session_state.filter_key != key:
        st.session_state.filter_key = key
        set_order(active)
        return

    # Otherwise keep the existing order/shuffle, but remove known/nonmatching cards.
    cleaned = [i for i in st.session_state.order if i in active_set]
    missing = [i for i in active if i not in cleaned]
    if cleaned != st.session_state.order or missing:
        st.session_state.order = cleaned + missing
        if st.session_state.order:
            st.session_state.pos %= len(st.session_state.order)
        else:
            st.session_state.pos = 0
        st.session_state.revealed = False


def current_idx() -> int | None:
    if not st.session_state.order:
        return None
    st.session_state.pos %= len(st.session_state.order)
    return st.session_state.order[st.session_state.pos]


def next_card() -> None:
    if st.session_state.order:
        st.session_state.pos = (st.session_state.pos + 1) % len(st.session_state.order)
    st.session_state.revealed = False


def mark_known(idx: int) -> None:
    """Mark as known and remove from queue immediately, until Reset progress."""
    st.session_state.known.add(idx)
    st.session_state.again.discard(idx)

    if idx in st.session_state.order:
        remove_at = st.session_state.order.index(idx)
        st.session_state.order.pop(remove_at)
        if not st.session_state.order:
            st.session_state.pos = 0
        elif remove_at < st.session_state.pos:
            st.session_state.pos -= 1
        elif st.session_state.pos >= len(st.session_state.order):
            st.session_state.pos = 0

    st.session_state.revealed = False


def shuffle_deck() -> None:
    """Shuffle the remaining queue without resetting to the original first card."""
    if len(st.session_state.order) <= 1:
        st.session_state.revealed = False
        return

    before = list(st.session_state.order)
    current = current_idx()
    random.shuffle(st.session_state.order)

    # If shuffle accidentally looks identical, rotate it once.
    if st.session_state.order == before:
        st.session_state.order = st.session_state.order[1:] + st.session_state.order[:1]

    # Also avoid keeping the same current card at the front.
    if st.session_state.order and st.session_state.order[0] == current and len(st.session_state.order) > 1:
        st.session_state.order.append(st.session_state.order.pop(0))

    st.session_state.pos = 0
    st.session_state.revealed = False


def restart_filtered_deck(category: str, search: str) -> None:
    set_order(active_indices(category, search))


def reset_progress(category: str, search: str) -> None:
    st.session_state.known = set()
    st.session_state.again = set()
    st.session_state.filter_key = (category, search.strip().lower())
    set_order(active_indices(category, search))


def render_prompt(card: dict, mode: str) -> tuple[str, str, str, str]:
    """Return mode label, CSS class, prompt text, and instruction."""
    if mode == "Hanzi → meaning":
        return (
            "Hanzi",
            "prompt-hanzi",
            card["hanzi"],
            "Say the pinyin, meaning, and one possible example sentence. Then click Reveal.",
        )
    if mode == "English → Hanzi":
        return (
            "Meaning",
            "prompt-english",
            card["english"],
            "Try to say or write the Chinese characters and pinyin. Then click Reveal.",
        )
    return (
        "Usage clue",
        "prompt-usage",
        card["usage"],
        "Guess the Chinese word that fits this usage. Then click Reveal.",
    )

# ============================================================
# Header and stats
# ============================================================
st.markdown(
    """
    <div class="hero">
        <p class="title">Chinese Flashcards</p>
        <p class="subtitle">
            Practice recognizing characters without pinyin first. Press <b>I knew it</b> to remove a card
            from practice completely until you use <b>Reset progress</b>.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

known_count = len(st.session_state.known)
again_count = len(st.session_state.again)
remaining_total = len(CARDS) - known_count

m1, m2, m3, m4 = st.columns(4)
for col, value, label in [
    (m1, known_count, "Known"),
    (m2, again_count, "Review again"),
    (m3, remaining_total, "Remaining"),
    (m4, len(CARDS), "Total cards"),
]:
    with col:
        st.markdown(
            f"<div class='metric-card'><div class='metric-value'>{value}</div><div class='metric-label'>{label}</div></div>",
            unsafe_allow_html=True,
        )

st.write("")

# ============================================================
# Filters
# ============================================================
f1, f2, f3 = st.columns([1.1, 1.1, 1.8])
with f1:
    mode = st.selectbox("Practice mode", ["Hanzi → meaning", "English → Hanzi", "Usage → Hanzi"])
with f2:
    category = st.selectbox("Category", CATEGORIES)
with f3:
    search = st.text_input("Search", placeholder="Try: 买, pinyin, school, transportation...")

sync_order(category, search)

if not st.session_state.order:
    st.success("No cards left in this filtered deck. You marked all matching cards as known.")
    if st.button("✦ Reset progress", type="primary", use_container_width=True):
        reset_progress(category, search)
        st.rerun()
    st.stop()

idx = current_idx()
card = CARDS[idx]
label, prompt_class, prompt_text, instruction = render_prompt(card, mode)

# ============================================================
# Main layout
# ============================================================
left, right = st.columns([1.65, 1], gap="large")

with left:
    # Important: this is rendered with unsafe_allow_html=True, not st.code/st.write.
    # That fixes the raw <div> code appearing inside the card.
    st.markdown(
        f"""
        <div class="study-card">
            <div class="card-top">
                <div class="pill">Card {st.session_state.pos + 1} / {len(st.session_state.order)}</div>
            </div>
            <div>
                <div class="mode-label">{e(label)}</div>
                <div class="prompt {prompt_class}">{e(prompt_text)}</div>
            </div>
            <div class="instruction">{e(instruction)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='caption-label'>Study actions</div>", unsafe_allow_html=True)
    with st.container(border=True):
        b1, b2, b3, b4, b5 = st.columns([1.05, 1.15, 1.25, .95, 1.05], gap="small")
        with b1:
            if st.button("👁 Reveal", type="primary", use_container_width=True):
                st.session_state.revealed = True
                st.rerun()
        with b2:
            if st.button("✅ I knew it", use_container_width=True):
                mark_known(idx)
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

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2, gap="small")
        with c1:
            if st.button("↺ Restart filtered deck", use_container_width=True):
                restart_filtered_deck(category, search)
                st.rerun()
        with c2:
            if st.button("✦ Reset progress", use_container_width=True):
                reset_progress(category, search)
                st.rerun()

with right:
    if st.session_state.revealed:
        examples_html = "".join(f"<div class='example'>{e(example)}</div>" for example in card["examples"])
        st.markdown(
            f"""
            <div class="answer-box">
                <div class="box-title">Answer</div>
                <div class="pinyin">{e(card["pinyin"])}</div>
                <div class="meaning">{e(card["hanzi"])} · {e(card["english"])}</div>
            </div>
            <div class="answer-box">
                <div class="box-title">Grammar / category</div>
                <div class="meaning">{e(card["category"])} · {e(card["part"])}</div>
            </div>
            <div class="answer-box">
                <div class="box-title">How to use it</div>
                <div class="muted">{e(card["usage"])}</div>
            </div>
            <div class="answer-box">
                <div class="box-title">Examples</div>
                {examples_html}
            </div>
            <div class="answer-box">
                <div class="box-title">Memory hint</div>
                <div class="muted">{e(card["hint"])}</div>
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
                    Pinyin, meaning, category, grammar notes, examples, and hints are hidden
                    until you press Reveal.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# Deck browser — collapsed by default for speed
# ============================================================
st.write("")
with st.expander("Deck browser", expanded=False):
    include_known = st.checkbox("Show known cards too", value=False)
    cards_to_show = browser_indices(category, search, include_known)
    st.caption(
        f"Showing {len(cards_to_show)} matching card(s). The browser stays collapsed by default to keep the app faster."
    )

    if cards_to_show:
        cols = st.columns(3)
        for n, card_i in enumerate(cards_to_show):
            deck_card = CARDS[card_i]
            if card_i in st.session_state.known:
                icon = "✅"
            elif card_i in st.session_state.again:
                icon = "🔁"
            else:
                icon = "•"
            with cols[n % 3]:
                st.markdown(
                    f"""
                    <div class="deck-card">
                        <div class="deck-hanzi">{icon} {e(deck_card["hanzi"])}</div>
                        <div class="deck-meta">{e(deck_card["pinyin"])} · {e(deck_card["english"])}</div>
                        <div class="deck-meta">{e(deck_card["category"])} · {e(deck_card["part"])}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

st.caption("Tip: ✅ cards disappear from practice immediately. They only return after Reset progress.")
