from slackbot.bot import listen_to

patterns = {
    "e": "工ｴｴｪｪ(´д｀)ｪｪｴｴ工",
    "g": "∠(｀・ω・´) goodデス！",
    "ga": "ヽ(｀Д´#)ﾉ ｶﾞﾝﾊﾞﾚ-",
    "h": "(^o^)／ ハイッ！",
    "hu": "( ´ー｀ )ﾌｩｰ．．．",
    "k": "ᕦ(ò_óˇ)ᕤ筋力！",
    "km": "щ(ﾟдﾟщ)ｶﾓｰﾝ",
    "n": "(ヾﾉ･∀･`)ﾅｲﾅｲ`)",
    "nrhd": "( ﾟ∀ﾟ)･∵. ﾅﾙﾎﾄﾞ!!",
    "oha": "(･ω･)/ｵﾊﾖ-",
    "ok": "ヽ(^o^)丿　OKOK!",
    "otu": "ヽ(=´▽`=)ﾉ ｵﾂｶﾚﾁｬｰﾝ",
    "r": "(*>_<*)ﾉ 了解デス",
    "s": "( ˘ω˘ )ｽﾔｧ",
    "tskn": "(σ・∀・)σ ﾀｼｶﾆ!!",
    "tu": "ﾍ( ´Д`)ﾉ ﾂｶﾚﾀ",
    "u": "Σヽ(｀д´；)ﾉ ウオォォ！",
    "w": "ﾍ(ﾟ∀ﾟﾍ)ワロタ",
    "wk": "((o(´∀｀)o))ﾜｸﾜｸ",
    "yr": "┐(´д｀)┌ﾔﾚﾔﾚ",
    "yy": "ヽ(^。^)ノﾜｲﾜｲ",
}

msg_pattern = r'^$'

for p in patterns:
    msg_pattern += '|^' + p + '$'

@listen_to(msg_pattern)
def res(msg):
    msg.send(patterns[msg.body['text']])

@listen_to(r'^help$')
def help_res(msg):
    res = ''
    for p in patterns:
        res += p + ":\t\t" + patterns[p] + "\n"
    msg.send(res)

