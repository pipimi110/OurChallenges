#-*-coding:utf-8-*-

from pwn import *

input_list = ["Don't you know about the bird? Everybody knows that the bird is the word!", "ord!birdhe whe? EveDon'ryt y birdbodyws thaout the  a know kno is tbout t", "he w knowt ybird knohe aord!bout tt the body bird is touryws thaDon'? Eve", "t yhe word!bout t knowDon'ou is t? Eve knows thabirdry birdhe abodyt the ", "Don'ry birdord! is t? Eve aou knows tha knowbout the wbodybirdhet the t y", " is t aDon'rybout t birdbody knoword!ou? Evebirdhews tha knot the t yhe w", " know? Evebird aoubodyhe w is tt the  knows thabout tord!ryDon't yhe bird", "ryt the  bird know aheoubirdws thaord!t y is tDon'bout t? Evehe wbody kno", " birdDon'he wrybout t? Eve aou knobirdt the t yhews thabody knoword! is t", "? Evehe knowbout t a birdt the Don' is tord! knoryt ybirdbodyouhe wws tha", "bird? Evebout t knowws thahe wt the  birdhet yryDon'ord! knoou is t abody", "ord!ws thabird a is t? Evehe wou knowrybout tt yt the  birdDon'hebody kno", " knot the ouDon'he word!rybirdbody knowws tha? Evet y is t a birdbout the", "ryws tha? Evet the Don' knobodyhe w birdbirdheou know at ybout t is tord!", " aheord!ws thabirdDon'bout tt yt the  is the w kno? Eve bird knowbodyryou", "ws thaord!t yheDon't the bodybout t is t knowourybird kno bird? Evehe w a", "bodybirdt yws thaDon'he wryord! is tt the  aou knobout t bird knowhe? Eve", "t the he abody kno bird is tws tha? Evehe wryord!Don'bird knowoubout tt y", "ord! know? Eve abody is the wDon'heryou knot y birdbirdbout tt the ws tha", " birdord!he? Evet the oubird about tDon't y knowws tha knoryhe wbody is t", "oubirdws thabodybout thehe word!Don't y is t bird? Evet the ry know a kno", " knowbout tt the Don'ord!he w? Evebird knobody aout yhe bird is tws thary", " knoord! a knowbout t birdhe wws thaheDon'? Evet the ryt y is tbodyoubird", "ws thaoubout tord!t the  is t kno knowhe whebody abirdryDon' birdt y? Eve", "bout tDon' is tt the ? Evet yhe word!ws thabody aouhe kno birdbirdry know", "bout the w know? Evet the  birdouryhews thaDon'bodyord! a kno is tbirdt y", " is tDon' aord!bout t knowry? Evehe w knobird birdt ybodyt the heouws tha", "het y? Evet the ord! a knobirdws thaou knowhe w birdry is tbout tbodyDon'", "ry? Evehe wws thaord! kno knowbodyout yhet the bout t a is tbirdDon' bird", "bout the bird knowt the ryouord!he wbodyt yws tha? Eve is tbirdDon' a kno", "bodyoubout t ahet the  kno knowt yord!ry? EveDon'he wbird is t birdws tha", "oubodyhe wDon't the  bird knobout t abirdws thahery knoword!? Evet y is t", "? Evehe wws tha abirdoubodyryord!t the  is t kno birdt y knowDon'hebout t", " know bird knohe ahe w is tbodyDon'? Eveord!t the t youbirdws thabout try", " is t ary know knoDon'ws thabird? Eve birdhe wt yt the hebout tord!bodyou", "ord!ws tha is t ahery kno knowouDon'bird? Evebodybout tt y birdt the he w", "ouord!bout t knot the  abirdws tha bird knowt yryhe whe is tbodyDon'? Eve", "? Eve birdbodybout t is the wt the ord!Don'ouws tha a knot ybird knowryhe", "bout t kno? Evebird at the hery is tbodyord!Don' knowws tha birdout yhe w", "ou abird knory? Evebout t birdord!t the body is the whet yws tha knowDon'", " knowbirdws thaouhe word!t y ahe bird is try? Evebout tDon' knot the body", " knowws tha is tt the t ybirdord!he wbodyouhe birdryDon'bout t a? Eve kno", " birdord!ou is thet y kno? EveDon' knowbodybirdt the bout t aws tharyhe w", " knowout yryheDon'bird bird? Eve is the wbodyws tha about t knoord!t the ", "t yhe is t knowbody? Eve knobout tt the  birdhe wDon'ord!ryws thaou abird", "birdt the  know kno is theDon'? Evebout tbody aord!ws thahe wry birdt you", "t the Don'bodybirdouws tha kno know birdheryt y a is the wbout tord!? Eve", "bout try? Evebody is t aws thaouord!t the  know birdhehe w knoDon'birdt y", "t y? EveDon'bout t kno is tws tharyord!bodybird at the  knowou birdhe whe", "he wws tha knowDon'out yord!t the bird? Evebout tbody bird ahe is try kno", "ws tha knowt yhe woubirdord! birdDon'ry knot the  is t? Evehebody about t", "ws tha knot the  is the wDon' birdou knoword!bout try? Evebirdhet y abody", " is t knowDon'? Eveouhe wbodybout thet the  birdord!t y kno aws thabirdry", "t the bodyry bird knowt y knoDon'birdbout tord!he w? Eveouhe is t aws tha", "ouord!t y knows tha knowrybird is tt the body ahe whebout tDon' bird? Eve", "bout tt y aord!heou knohe w? Every knowt the ws tha birdDon' is tbodybird", "bodyhe bird knowbout t knobirdws thahe w a? Evet y is tryord!t the ouDon'", "Don'out the he word!bird kno know? Evebout tt y is tbody birdws tha ahery", " birdord!ry? Evehehe wt the bodyou know is tws tha knoDon'bout tbirdt y a", " bird is tout the herybodyord! knobout tDon' know? Evews thabirdt y ahe w", "ws thabirdhe w aord!body is theou kno birdbout t? Evet the Don'ryt y know", "he wws thaord!Don'? Eve at y birdbout t is t knobird knowbodyryhet the ou", " is t? Eve at yhews that the bout tord!ryou knobodyDon' knowbird birdhe w", "ws that the hebodyt y? Eve kno a bird is tDon'ouhe w knoword!rybout tbird", "birdDon' knowt yhe whe is tws that the  aou knobout tbodyord!? Every bird", " abirdou know kno is tbout the w? EveDon'ord!ws that yhebodyry birdt the ", "het y knobirdt the ord!oubodyws thahe wDon' a is t knowry bird? Evebout t", "ryt the  knoheDon' is tbout tord!he wout ybirdbody a? Evews tha know bird", "ord!bout the wt yhe? Evebody knowws tha is tDon'ou birdt the ry a knobird", "he wws that the  kno birdt y is tDon' about tord!bodybirdoury knowhe? Eve", "? Everybody birdhe knot yws thaouhe wbird a knoword!t the bout tDon' is t", "ws thaou is try? Evehebout tbird knowDon't the t y knobody birdord!he w a", " a knobody is tt you? Eve birdws tha knowryhe wt the heDon'bout tbirdord!", " is tt ybout t? EveoubirdDon'bodyheryord! birdhe wt the  knows tha know a", "t the bout tt you birdhe whe know? EveDon'ws thaord! is t knobodybird ary", "ord! is tws tha birdhe abirdt yDon'he w? Eveourybout t knot the body know", "? EveryheDon' is tbirdhe w birdt the ord! know abodyws that y knobout tou", " birdhe knorybirdt yhe wbout tws tha knowou? Eve is tbody aord!t the Don'", "ws thahe wDon'bird? Eveheord!ry birdt the  kno is tbout t knowbody aout y", " is t kno? Evehe w knowws tha aout ybout tbodyry birdord!hebirdt the Don'", "t yt the ry is tbout t a know? EvebirdbodyDon' knohe w birdouws thaheord!", "birdbout tws that y birdout the he wbody knowry? Eveord!he aDon' is t kno", " knoword!t ybodyt the ws tha bird abirdbout t is the w knoryouheDon'? Eve", "ryt the  a birdbirdord! kno knowbodyDon' is tws thaouhe wbout tt y? Evehe", "ord!bodyDon' is the birdbirdryhe w know aou kno? Evet the ws that ybout t", "? Evebird is tord! knowhe a knows tha birdbout tt yt the he wryDon'bodyou", "ry knowbout tt the ws tha? Eve is the abodyDon'birdou birdhe wt yord! kno", " knoDon'bout tryt the ouhe w a birdhe is tbody know? Evebirdws thaord!t y", "ord! kno? Evebout t is t know birdoubirdDon'heryws thahe w abodyt yt the ", "ry at the he is t bird kno? Evews thabout tbodybirdDon'ouord!he w knowt y", "oubody a knowhe is tt yt the ryws thaord!? EvebirdDon' bird knohe wbout t", "ord!he know a knot ybout tbodyws thary bird is the w? Evebirdt the ouDon'", "Don' kno birdord!ws thaou is tbout tbird knowt yhe w ahe? Everybodyt the ", " birdbirdry is t aord!Don'bodyt ybout tt the  knohe? Eveouws thahe w know", "he wt y knowrybird is t knot the body birdbout tord!ws thaDon'he? Eveou a", "t the bout tt ybody aouws tha knowbird is the w birdryheord!Don' kno? Eve", " knot the  birdbout tbodyhe w is tws tharyou? Eveord! at ybirdheDon' know", " knowDon'? Eve is the wrybirdbody a knohews that yout the bout t birdord!", "ws that the  at ybird know kno birdheryord!he wDon' is tbout tbody? Eveou", "t the birdhe wbout t is t? EveheDon' know knobody aout y birdord!ryws tha", "Don' knowws thabodyord! is tbout t birdryhe wt yhe a knobirdt the ? Eveou", "ouws thahe w a knoword!ry is tt the Don' kno? Evet ybout thebird birdbody", "? Eve knobodyt the Don' knowry a birdou is tws thabirdord!t yhehe wbout t", "ws thahe wbout t? Eveord!t the  know birdhebodybird is touryDon' knot y a", "hebirdhe wt yryord! knoouws tha bird is tbody a know? Evet the bout tDon'", "ouhe w know? Evet yryDon'bout tord!ws thabody is tt the  knobirdhe bird a", " abodyDon' knowt yt the bout tbirdheord! knory? Eveouws tha birdhe w is t", " knowt yDon' a is t? Evebodyws thaord!t the he wbout tbirdry bird knoheou", "bout t is t birdt yord!he know? Evebirdbodyouws that the Don' knohe wry a", "Don'ord! birdouhe wryt the bout t? Eve knowbirdt yhe knows thabody a is t", " knows tha is tDon'body? Eve birdheord!he wouryt the bout tt y know abird", " a knohe w is tbirdbody knowws thaou birdbout thet yryord!Don't the ? Eve", "ryt ybout tord! kno abodyhe whews tha bird is tt the ouDon'bird? Eve know", "rybodyws thahebird birdt the Don' about tord!he w know is t knoout y? Eve", "ou arybodyhe w kno birdt yws that the bout theDon'ord! know is t? Evebird", "ryws tha bird know? EveDon'ord!oubout t a is the wbodyhebird knot yt the ", " birdt y? Evebirdbody knowhe word!t the Don' knory is t aoubout tws thahe", "he is tbout t? Eveou kno at the body birdbirdt yord!Don'ry knowws thahe w", "t the heDon'ws thahe wbout tbirdbody is t? Eveouryord! a bird knot y know", " knowt y knot the he w birdbodybout tryhe? Eveouws tha is t aDon'birdord!", "t y kno is tryord!? EveDon'bird knowbout touhe birdt the  aws thabodyhe w", "birdbody bird aws tharyt the Don'ouord!he wt ybout t? Eve kno is t knowhe", "ou knowbodybird is t aryhe whebout t? Evews thaDon'ord!t y kno birdt the ", "he wbodybout t knowt yhery birdt the  aord!Don' kno? Eve is tbirdouws tha", " knobout t is tbody knowhe w? Evet ybirdry birdt the ws thaheouDon' aord!", " is t? Every knobird know birdws thaDon'bout theouhe wt the ord!bodyt y a", "ouhe w knowryws tha bird a is t kno? EveDon'birdt yord!bodybout thet the ", " is t knot the bodyord!t y birdDon'herybirdws thabout the w aou know? Eve", "birdbout tou ary is t? EvebodyDon'heord! kno birdt yt the ws tha knowhe w", " is tord!ws tha? Evet the oubird abody birdry knowbout tDon't yhehe w kno", " about t knot the ord!t y? Everybirdws tha knowoubody is tDon' birdhe whe", "he wbird a? Eve knoword!bodyt the ws that yheryoubout t knoDon' is t bird", "bout t knowDon'bird bird a? Eveord!ou knobody is the wryt yt the hews tha", "heou a know knoDon'bodybout t? Evet yhe w birdord!bird is tryws that the ", "t the  is t knoout yhebout the w aord! knowDon'birdws tha bird? Evebodyry", "ryt the  is tbirdt y a? Evebout t knoouord!he wDon'he knowbody birdws tha", "? Eve knowhe wDon' kno is tbout tbirdbodyt the het y bird aws thaord!oury", "ws tha? Evebirdbout t knohery know birdbodyord!t the  is touhe w aDon't y", "ouord!Don'rybodyhe wt yws tha is t? Evet the  kno knowbird birdbout the a", " is tt youord!bout t bird knoDon'? Evet the herybirdws thabodyhe w a know", "t the he know? Evebirdoubody knoDon' aord! birdws that ybout try is the w", "birdDon'ws thabodyt yhehe w know? Evebout t bird knoord!t the  is t aoury", " a is t? Evehe w knoword!t the heDon' birdout ybodybout try knows thabird", "bird arybodyt the  knowou is tbout the wws thahe? Evet y knoDon'ord! bird", "he w knohery birdbodyDon'bird? Eve at yt the  is tbout tord!ou knowws tha", "birdord!bout tDon'? Eve knohe whe bird knowbodyt yws tharyt the  is tou a", "bout tou? Eve birdws that the t yord! knobodyDon'bird a knowryhe w is the", "he wws tha bird a knorybout tDon'bodyord!birdt yhe is t? Evet the ou know", "t the bout the w birdDon'? Every kno is t aord!ouws thabird knowhebodyt y", "heord! a is tws thabout tryDon'ouhe wbird birdt the ? Evet y knowbody kno", " knowou? Evet the  kno is the wryt yws thaDon' abirdbodybout t birdord!he", "he wt yord!? Evehe knobird is tbout trybody knowDon't the  birdws tha aou", " knoword!out y birdhehe wbout try? Evews thabody kno aDon't the  is tbird", "Don' bird? Every aord!t yhe wws tha knot the bout tbird knowouhebody is t", " is tDon' knowbody? Eve a knobirdhe wt yt the oubout t birdws tharyheord!", "t yws tha at the  bird know? EveDon'bodybout t is t knoryhe wheouord!bird", " birdheourybodyt yhe wws thaDon'? Eveord!bout tbirdt the  is t a kno know", "bout t kno? EveDon'bird is tt the he w knowws thabodyhe birdord!t youry a", "ryt ybody knooubout the w birdheDon'ord!ws tha is tbird at the ? Eve know", "he w a knohet the t yry? Evebirdbout t is tbody birdws tha knoword!Don'ou", " birdDon' knobirdhehe wws tha is t know? Evebout t abodyryout the t yord!", " birdbody ahe knows thaouhe word!t y knowbout try is tt the bird? EveDon'", "ws thaouDon'ord! is t? Evehe w abody birdbirdt yrybout t knowt the  knohe", " birdbodybout t knowt y is tord!? Eve knobirdryhe wDon'ws thahe at the ou", "he wDon't yord!he birdws that the ? Evebodybird is tbout try kno knowou a", "t the bout t knoouord!he birdt yDon'? Evebirdbody ahe wws tha is t knowry", " bird knowrybout tt the ws thahe wDon'? Evet yord! knoouhebodybird a is t", "Don'he w is t knowbodybout try? Evehews thaouord!birdt the  a bird knot y", " birdoubirdbodyhe w ahe kno? Eve knowbout t is tt the ryt yDon'ws thaord!", " is t? Evet yt the ws thahe woubout tbody knoord! know birdbird aryDon'he", "rybody knowDon'he wt the ? Eveouord! birdbird knobout t is the aws that y", "Don'birdouws thaord! know at the  is the kno? Evebout tryt y birdbodyhe w", "birdt yord! is the wbody kno about t knowhews thaou? Eve birdt the Don'ry", " bird knot the bout the wbirdbodyou is theryt y aws thaDon'? Eveord! know", "ws tharyord! is t knowhe w? EvebodybirdDon't yheou a birdbout t knot the ", "body? Eve know knot the  is tbirdt y aryouord!bout tDon'he whews tha bird", "he at the  know knohe wou is tbirdt yDon'ws tha birdbodyord!bout try? Eve", "t y birdt the he know a? Every is t knobout tbirdord!ouws thahe wDon'body", "? EveDon' know is toubout tt the  at yryhe wws tha birdbirdheord!body kno", "bout tt y birdDon'rybodyhet the  kno knowbirdou ahe w? Eve is tord!ws tha", " is thews tha knobout tryhe word! a? Evet the  birdt you knowbodybirdDon'", "t the  is thews thaout yord!bout tDon' abird? Eve knory know birdbodyhe w", "ord! knowbout touDon'bodyt yws tha ahehe wbirdt the ? Every is t bird kno", "ord!bout t at yhe know knobodyou birdws thahe wt the rybird? Eve is tDon'", "he arybout t knows thaDon't yhe wbody birdbirdord!ou? Eve is tt the  know", "birdt the he birdws thahe w about tbodyDon' is tord!ry? Eve knowout y kno", " is try know a kno birdDon'bird? Evet ybodyheouord!ws that the he wbout t", "bout tbodyhehe wDon'? Eve birdws thabird ary is tt yout the ord! know kno", " knohet ybout tDon't the  a birdouryhe wbodyord!? Evews tha knowbird is t", "body knoheord!ou a is tws tharyhe w? Evet yt the bird birdbout t knowDon'", " is tt the Don'hews tha know a? Eve knoryoubodyord!t ybout the w birdbird", "t the  knows tha abirdDon' birdhehe w is tbody? Eveoubout tord! knowt yry", "t the birdbout tord!he birdouhe wt yws tha? Eve aryDon' is tbody kno know", " birdbout t at the t you know knobirdheord!? Evews tha is tbodyhe wryDon'", " is t knowbody birdws thabout tDon't the  knot yhe w aord!? Eveouryhebird", "t the  is tt yhe wbout tord!he knowws thabodyryDon'ou knobird bird a? Eve", " birdryt ybout tDon'bird knohe w know is t ahe? Evews thaord!t the bodyou", "ou kno? Eve bird is t about tDon'ord! knowt ybodybirdhe wryhews that the ", " a is the wbirdhe? Eve knows that yry birdord!oubout tt the body knowDon'", "ry know birdt yDon' knot the  is tbody ahebirdord!oubout t? Evehe wws tha", " birdryws thabout t is tbody aDon'? Eve knot yhehe word! knowbirdt the ou", "ws tha? Evebird is the wt yt the  birdbody knowry knoou aheord!Don'bout t", "birdhe w at the bout tbody knowDon'ryws thahe is tord!? Eveou birdt y kno", "Don'bird? Eve ahe knowt the he w is tryord!oubout tws tha knobody birdt y", "birdbout t knowt the t y abodyord!ws tha bird kno? EveouDon'hery is the w", " knowbirdhe wou knobody is tt the bout tws tharyt yDon' aheord!? Eve bird", "ord! kno is tbirdbodyryDon'he whe knowt youws thabout tt the ? Eve bird a", "? Evehe a bird knobirdhe wt y is tws tha knoword!oubodyt the rybout tDon'", "bird? Evebout t knowbody is tDon'he wheou knot the ryord! bird at yws tha", "ord!t y knowbout touhe a? Every knoDon' is tbirdbodyws tha birdhe wt the ", " aws thaDon't yhebirdbodybout t birdord!t the ou is the wry know? Eve kno", " kno ahe w? Evet the  birdDon't yord!ry know is tbodyhebirdws thaoubout t", "ryou bird kno is t knowt the Don'bodyhe wbout tbirdt y aws thaord!? Evehe", "ryt the ? Evebout tord! kno know is tbodyws thaheDon'he wbirdt you a bird", "t y? Eve knobodyryhe w birdbout tbirdhet the ws tha a is touDon' knoword!", "Don' birdhe wt the birdry? Eve knowbody kno about tt yhews tha is tord!ou", "bout tbird birdws tha is tbodyt the t you ary knoword!Don'he knohe w? Eve", "? Evebout touhe w birdry knohe is tbodyDon'ws thabirdord! know at yt the ", "ord! knowbodybout tDon' birdbirdhe w a kno is tryt yws that the heou? Eve", " knoDon'? Eve aord!t yrybirdbout t is tbodyt the he birdws tha knowouhe w", "he knohe wry knowbout tt yDon' birdws tha? Eve is tou at the bodybirdord!", " knoou? Evebird at the ws tharybody knoword!bout tt y is theDon' birdhe w", " is t knobodyt yt the  birdryhe? Eveord! aouhe w knowbout tws thaDon'bird", "body? Everybout t is t knoout ybird a birdhe wDon'ord!het the  knowws tha", "ryouws thabody a? Evehe birdDon' knowt the bout tbirdhe w knot yord! is t", " is try at the  knowDon't y knobout the? Evebody birdws thahe wbirdord!ou", "birdbout tt y ary knowhe is t birdDon'ws thahe wou knot the ? Eveord!body", "body bird is tryout y? Eveheord!t the  kno knowws thabout tDon' ahe wbird", "t the  knows thahe w aord! is tbody knowDon't y? Evebird birdryoubout the", " knowt the hebirdry knoou is tbodyws tha? Evet y about tDon'he word! bird", "Don' knowry? Evehe w about tbirdt yhe birdouws thaord!body is tt the  kno", "ouDon' is tbout t kno birdhe wt the ord!bodyry a? Evet y knowhews thabird", "t yhe wbout touhe? Evet the  is tDon' know abody bird knobirdws thaord!ry"]

assert len(input_list) == 233

p = process('./damnV')
# context.log_level = 'debug'
for line in input_list:
    p.sendline(line);
print p.recvall()
# p.interactive()
