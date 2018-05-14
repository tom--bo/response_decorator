from slackbot.bot import listen_to
    
@listen_to(r'^h$')
def res_h(message):
    message.send("(^o^)／ ハイッ！")

@listen_to(r'^r$')
def res_r(message):
    message.send("(*>_<*)ﾉ 了解デス")

@listen_to(r'^g$')
def res_g(message):
    message.send("∠(｀・ω・´) goodデス！")

@listen_to(r'^yr$')
def res_yr(message):
    message.send("┐(´д｀)┌ﾔﾚﾔﾚ")

@listen_to(r'^u$')
def res_u(message):
    message.send("Σヽ(｀д´；)ﾉ ウオォォ！")

@listen_to(r'^w$')
def res_w(message):
    message.send("ﾍ(ﾟ∀ﾟﾍ)ワロタ")

@listen_to(r'^wk$')
def res_wk(message):
    message.send("((o(´∀｀)o))ﾜｸﾜｸ")

@listen_to(r'^tskn$')
def res_tskn(message):
    message.send("(σ・∀・)σ ﾀｼｶﾆ!!")

@listen_to(r'^s$')
def res_s(message):
    message.send("( ˘ω˘ )ｽﾔｧ")

@listen_to(r'^otu$')
def res_otu(message):
    message.send("ヽ(=´▽`=)ﾉ ｵﾂｶﾚﾁｬｰﾝ")

@listen_to(r'^hu$')
def res_hu(message):
    message.send("( ´ー｀ )ﾌｩｰ．．．")

@listen_to(r'^tu$')
def res_tu(message):
    message.send("ﾍ( ´Д`)ﾉ ﾂｶﾚﾀ")

@listen_to(r'^n$')
def res_n(message):
    message.send("(ヾﾉ･∀･`)ﾅｲﾅｲ`)")

@listen_to(r'^ga$')
def res_ga(message):
    message.send("ヽ(｀Д´#)ﾉ ｶﾞﾝﾊﾞﾚ-")

@listen_to(r'^ok$')
def res_ok(message):
    message.send("ヽ(^o^)丿　OKOK!")

@listen_to(r'^yy$')
def res_yy(message):
    message.send("ヽ(^。^)ノﾜｲﾜｲヽ(^。^)ノﾜｲﾜｲ")

@listen_to(r'^k$')
def res_k(message):
    message.send("ᕦ(ò_óˇ)ᕤ筋力！")

@listen_to(r'^km$')
def res_km(message):
    message.send("щ(ﾟдﾟщ)ｶﾓｰﾝ")

@listen_to(r'^e$')
def res_e(message):
    message.send("工ｴｴｪｪ(´д｀)ｪｪｴｴ工")

