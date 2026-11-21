# -*- coding: utf-8 -*-
"""Builds docs/playground/bank-lernen.json: learning-only content (no timers, every item explained in English)."""
import json, os
G1 = [
{"id":"s1a","title":"Invitation to a birthday","intro":"Personal letter. Pick a, b or c. Tap an option to see why it is right or wrong.",
 "text":"Liebe Anna,\n\nich hoffe, es geht {1} gut. Ich möchte dich {2} meinem Geburtstag einladen. Die Party ist am Samstag und beginnt {3} 18 Uhr. Leider {4} ich nicht viel Platz, deshalb bringe bitte keine Freunde mit. Ich {5} mich sehr, wenn du kommst.\n\nViele Grüße\nTom",
 "gaps":[
  {"o":["dir","dich","du"],"ok":0,"why":"**gehen + Dativ**: *Wie geht es dir?* The person who feels well is in the dative (mir, dir, ihm). *dich* is accusative and *du* is nominative, so both fail."},
  {"o":["zu","für","auf"],"ok":0,"why":"**einladen zu + Dativ**: *zu meinem Geburtstag* (zu + dem = zum). *einladen für* and *auf* do not exist as fixed pairs.\nLearn it as a block: *jemanden zu etwas einladen*."},
  {"o":["um","in","am"],"ok":0,"why":"Clock time uses **um**: *um 18 Uhr*. *am* is for days (am Samstag) and *in* for months or years."},
  {"o":["habe","bin","werde"],"ok":0,"why":"**Platz haben** = to have room. *sein* and *werden* cannot take a noun object like this. *Leider* opens the sentence, so the verb stays second: *Leider habe ich ...*."},
  {"o":["freue","freust","freut"],"ok":0,"why":"**sich freuen**, ich-form: *ich freue mich*. *freust* belongs to du and *freut* to er/sie/es."}]},
{"id":"s1b","title":"Cancelling because of illness","intro":"Personal letter. A polite *Absage* (decline) with a reason.",
 "text":"Lieber Max,\n\nvielen Dank {1} deine Einladung. Leider kann ich nicht kommen, {2} ich krank bin. Ich habe {3} Fieber und muss im Bett bleiben. Vielleicht können wir uns nächste Woche {4}? Ich wünsche dir {5} Party!\n\nBis bald\nPaul",
 "gaps":[
  {"o":["für","an","auf"],"ok":0,"why":"**danken / Dank für + Akkusativ**: *vielen Dank für deine Einladung*. This is the standard opening of a reply."},
  {"o":["weil","denn","deshalb"],"ok":0,"why":"The verb *bin* is at the end, so this is a subordinate clause and needs **weil**.\n*denn* would need the verb in second place (*denn ich bin krank*). *deshalb* gives a result, not a reason."},
  {"o":["hohes","hohe","hohem"],"ok":0,"why":"*Fieber* is neuter (das Fieber). *Ich habe* takes the accusative. No article, neuter accusative = adjective ending **-es**: *hohes Fieber*."},
  {"o":["treffen","trifft","getroffen"],"ok":0,"why":"**können + infinitive at the end**: *wir können uns treffen*. After a modal verb the second verb is always an infinitive."},
  {"o":["eine schöne","einen schönen","ein schöne"],"ok":0,"why":"*die Party* is feminine. Accusative feminine = **eine schöne Party**. *einen* is masculine and *ein schöne* has the wrong ending."}]},
{"id":"s1c","title":"New flat and moving help","intro":"Personal letter. Prepositions, *und* and a polite question.",
 "text":"Hallo Lena,\n\nich habe eine neue Wohnung gefunden! Sie ist nicht weit {1} dem Zentrum, nur zehn Minuten {2} Bahnhof. Die Wohnung hat zwei Zimmer {3} einen Balkon. Am Samstag {4} ich umziehen. {5} du mir helfen?\n\nLiebe Grüße\nSara",
 "gaps":[
  {"o":["von","aus","zu"],"ok":0,"why":"**weit von + Dativ**: *nicht weit vom Zentrum* (von dem = vom). *aus* means out of and *zu* means to."},
  {"o":["zum","zur","am"],"ok":0,"why":"*der Bahnhof* is masculine: *zu + dem = zum Bahnhof* (going to). *zur* is for feminine nouns (zur Schule). *am Bahnhof* means at the station, not the distance to it."},
  {"o":["und","aber","sondern"],"ok":0,"why":"Two things the flat has are added together: **und**. *aber* shows a contrast and *sondern* follows a negation."},
  {"o":["möchte","möchten","möchtest"],"ok":0,"why":"**ich möchte**. *möchten* is for wir/sie/Sie, *möchtest* is for du. Modal verb in second place, infinitive *umziehen* at the end."},
  {"o":["Kannst","Kann","Könnt"],"ok":0,"why":"Yes/no question: verb first. With **du** the modal is *kannst*. *Kann* is er/sie/es and *Könnt* is ihr."}]}]
G2 = [
{"id":"s2a","title":"Applying for a flat","box":["um","seit","besonders","einen","wäre","ob","denn","bei"],
 "intro":"Formal letter. Choose a word from the box for each gap. Three words are extra.",
 "text":"Sehr geehrter Herr Müller,\n\nhiermit möchte ich mich {1} die Wohnung in der Hauptstraße bewerben. Ich arbeite {2} drei Jahren als Ingenieur und habe ein festes Gehalt. Die Wohnung gefällt mir {3} gut, weil sie hell und ruhig ist. Könnten wir {4} Besichtigungstermin vereinbaren? Ich {5} Ihnen sehr dankbar, wenn Sie mir bald antworten würden.\n\nMit freundlichen Grüßen\nA. Kumar",
 "gaps":[
  {"ok":"um","why":"**sich um etwas bewerben**: *sich um eine Wohnung / um eine Stelle bewerben*. Learn the verb with its preposition."},
  {"ok":"seit","why":"**seit + Dativ** for something that started in the past and still continues: *seit drei Jahren* (note the -n in the dative plural). *bei* does not give a time span."},
  {"ok":"besonders","why":"*besonders gut* = especially well. A degree word before an adjective or adverb. *denn* is a conjunction and would not fit here."},
  {"ok":"einen","why":"*der Termin* is masculine, accusative after *vereinbaren*: **einen Besichtigungstermin**."},
  {"ok":"wäre","why":"**Ich wäre dankbar, wenn ...** is the polite Konjunktiv II of *sein*. It sounds much more formal than *ich bin dankbar*. A very useful exam phrase."}]},
{"id":"s2b","title":"Complaint about an invoice","box":["wegen","dass","vor","jedoch","bald","weil","damit","oder"],
 "intro":"Formal letter. Choose a word from the box for each gap. Three words are extra.",
 "text":"Sehr geehrte Damen und Herren,\n\nich schreibe Ihnen {1} der Rechnung vom 5. Mai. Ich habe festgestellt, {2} der Betrag zu hoch ist. Ich habe den Vertrag {3} vier Wochen abgeschlossen und zahle 29 Euro im Monat. In der Rechnung stehen {4} 39 Euro. Bitte prüfen Sie das und schicken Sie mir {5} eine neue Rechnung.\n\nMit freundlichen Grüßen\nB. Roy",
 "gaps":[
  {"ok":"wegen","why":"**wegen + Genitiv** (or dative in speech) = because of / concerning: *wegen der Rechnung*. A standard opening of a complaint."},
  {"ok":"dass","why":"After *feststellen* comes a content clause with **dass**, verb at the end: *..., dass der Betrag zu hoch ist*. *weil* would give a reason, which is not meant here."},
  {"ok":"vor","why":"**vor + Dativ** with a time = ago: *vor vier Wochen*. Do not confuse it with *seit* (since, still going on)."},
  {"ok":"jedoch","why":"*jedoch* = however. It can sit in position 1 or inside the sentence without changing the verb position: *In der Rechnung stehen jedoch 39 Euro*."},
  {"ok":"bald","why":"*schicken Sie mir bald* = please send me soon. An adverb of time fits; *damit* and *oder* would need a clause."}]}]
FIX = [
("Ich möchte gehen zum Arzt.","Ich möchte zum Arzt gehen.","With a modal verb (möchte, kann, muss) the second verb is an infinitive and it goes to the **end**.",
 [("Ich möchte zum Arzt gehen.",1),("Ich gehen möchte zum Arzt.","Two verbs next to each other at the front. The modal must stay in second place."),("Ich möchte gehen zum Arzt.","This is the sentence from the exercise, the infinitive is not at the end yet.")],"Verb position"),
("Weil ich bin krank, bleibe ich zu Hause.","Weil ich krank bin, bleibe ich zu Hause.","After **weil** the conjugated verb goes to the end of the clause.",
 [("Weil ich krank bin, bleibe ich zu Hause.",1),("Weil ich bin krank, ich bleibe zu Hause.","Two mistakes: the verb stays in the middle of the weil clause and the main clause lacks inversion."),("Weil ich krank bin, ich bleibe zu Hause.","The weil clause is right, but after it the main clause must start with the verb (bleibe ich).")],"Nebensatz"),
("Ich habe gestern gearbeitet lange.","Ich habe gestern lange gearbeitet.","In the Perfekt the participle (gearbeitet) closes the sentence. Everything else goes **between** haben and the participle.",
 [("Ich habe gestern lange gearbeitet.",1),("Ich habe gearbeitet gestern lange.","The participle must be last."),("Ich gestern habe lange gearbeitet.","The verb must be in second place, directly after Ich.")],"Perfekt"),
("Ich danke dir für dein Brief.","Ich danke dir für deinen Brief.","*für* always takes the accusative. *der Brief* is masculine, so *dein* becomes **deinen**.",
 [("Ich danke dir für deinen Brief.",1),("Ich danke dir für deinem Brief.","Dative is wrong after für, because für always takes the accusative."),("Ich danke dir für deiner Brief.","*deiner* is feminine dative or genitive, not accusative masculine.")],"Akkusativ"),
("Ich wohne seit zwei Jahre in Aachen.","Ich wohne seit zwei Jahren in Aachen.","**seit** takes the dative. In the dative plural the noun gets an extra **-n**: die Jahre → seit zwei Jahren.",
 [("Ich wohne seit zwei Jahren in Aachen.",1),("Ich wohne seit zwei Jahre in Aachen.","This is the sentence from the exercise."),("Ich wohne für zwei Jahren in Aachen.","*für* does not express 'since'. Use seit for time that is still going on.")],"Dativ"),
("Ich gehe in der Schule.","Ich gehe in die Schule.","**Wohin?** (movement) with in takes the accusative: *in die Schule*. **Wo?** (location) takes the dative: *in der Schule*.",
 [("Ich gehe in die Schule.",1),("Ich gehe zu die Schule.","*zu* is followed by the dative: *zur Schule*, not zu die."),("Ich gehe an der Schule.","*an der Schule* would mean at the school, and the question is still wohin.")],"Wechselpräposition"),
("Können Sie mir helfen bitte?","Können Sie mir bitte helfen?","The infinitive *helfen* must be at the end. Politeness words like *bitte* go inside the sentence.",
 [("Können Sie mir bitte helfen?",1),("Sie können mir bitte helfen?","This is not a question form. A yes/no question starts with the verb."),("Können Sie helfen mir bitte?","The infinitive must be last and the object *mir* stays before it.")],"Verb position"),
("Ich habe gestern nach Köln gefahren.","Ich bin gestern nach Köln gefahren.","Verbs of movement (fahren, gehen, kommen, fliegen) form the Perfekt with **sein**.",
 [("Ich bin gestern nach Köln gefahren.",1),("Ich habe gestern nach Köln gefahren.","*fahren* with a destination needs sein."),("Ich war gestern nach Köln gefahren.","*war* ... gefahren is the Plusquamperfekt, which is not meant here.")],"Perfekt mit sein"),
("Sehr geehrter Frau Schmidt,","Sehr geehrte Frau Schmidt,","In a formal letter the greeting must agree with the gender: **Sehr geehrte Frau**, **Sehr geehrter Herr**. This is a typical Schreiben mistake.",
 [("Sehr geehrte Frau Schmidt,",1),("Sehr geehrten Frau Schmidt,","*geehrten* is for the accusative or dative and is used in a different greeting, not here."),("Liebe Frau Schmidt,","Too personal for a formal letter. Use *Sehr geehrte ...* instead.")],"Briefform"),
("Ich möchte Sie fragen, ob können Sie mir helfen.","Ich möchte Sie fragen, ob Sie mir helfen können.","**ob** introduces an indirect yes/no question: the verb goes to the end, here the modal *können*.",
 [("Ich möchte Sie fragen, ob Sie mir helfen können.",1),("Ich möchte Sie fragen, ob können Sie mir helfen.","This is the sentence from the exercise."),("Ich möchte Sie fragen, ob Sie können mir helfen.","The modal verb has to be last, after the infinitive.")],"Nebensatz"),
("Ich warte für den Bus.","Ich warte auf den Bus.","**warten auf + Akkusativ** is a fixed pair. Learn verbs together with their preposition.",
 [("Ich warte auf den Bus.",1),("Ich warte an den Bus.","*an* does not fit with *warten*."),("Ich warte auf dem Bus.","The preposition is right, but *warten auf* needs the accusative (den).")],"Verb + Präposition"),
("Ich habe keine Zeit, deshalb ich kann nicht kommen.","Ich habe keine Zeit, deshalb kann ich nicht kommen.","**deshalb** is a connecting adverb. It takes position 1, so the verb follows right after: *deshalb kann ich*.",
 [("Ich habe keine Zeit, deshalb kann ich nicht kommen.",1),("Ich habe keine Zeit, deshalb ich nicht kommen kann.","Verb at the end is for weil, dass, ob. *deshalb* is not one of them."),("Ich habe keine Zeit, weil kann ich nicht kommen.","*weil* sends the verb to the end and does not fit the meaning (cause and effect are reversed).")],"Konnektoren"),
("Das ist ein sehr nette Frau.","Das ist eine sehr nette Frau.","*Frau* is feminine, so the article is **eine**. The adjective *nette* gets -e.",
 [("Das ist eine sehr nette Frau.",1),("Das ist einen sehr nette Frau.","*einen* is for masculine accusative, not feminine."),("Das ist ein sehr nettes Frau.","The article stays wrong and *nettes* is neuter.")],"Artikel"),
("Ich interessiere mich für der Kurs.","Ich interessiere mich für den Kurs.","*sich interessieren für + Akkusativ*. *der Kurs* is masculine, accusative = **den Kurs**.",
 [("Ich interessiere mich für den Kurs.",1),("Ich interessiere mich an den Kurs.","*interessieren an* does not exist. The fixed pair is *für*."),("Ich interessiere mich für dem Kurs.","*dem* is dative. After *für* you need the accusative.")],"Verb + Präposition"),
("Am Montag ich habe einen Termin.","Am Montag habe ich einen Termin.","If a time phrase opens the sentence, the verb stays in **second place** and the subject follows (inversion).",
 [("Am Montag habe ich einen Termin.",1),("Am Montag einen Termin habe ich.","Only one element can stand before the verb."),("Am Montag ich einen Termin habe.","Verb at the end only happens in a subordinate clause.")],"Inversion"),
("Ich kann nicht kommen, weil ich muss arbeiten.","Ich kann nicht kommen, weil ich arbeiten muss.","With **weil** the verbs go to the end, and the modal verb stands last: *arbeiten muss*.",
 [("Ich kann nicht kommen, weil ich arbeiten muss.",1),("Ich kann nicht kommen, weil muss ich arbeiten.","The verb is not at the end."),("Ich kann nicht kommen, weil ich muss arbeiten.","This is the sentence from the exercise.")],"Nebensatz")]
def ff(it):
    w,r,why,opts,tag=it
    return {"wrong":w,"right":r,"why":why,"tag":tag,"o":[{"t":o[0],"ok":1 if o[1]==1 else 0,"n":"" if o[1]==1 else o[1]} for o in opts]}
FR = [
{"id":"f1","sec":"schreiben","title":"Opening and closing a letter","when":"Every Schreiben and every Sprachbausteine letter starts and ends like this. Easy points for Formal accuracy.",
 "items":[("Sehr geehrte Damen und Herren,","Formal letter to an unknown person or company. Capital S is not needed after the comma, the next line starts small."),
  ("Sehr geehrter Herr Müller, / Sehr geehrte Frau Schmidt,","Formal letter to a named person. Match the gender."),
  ("Liebe Anna, / Lieber Max,","Friend or family (du). Use *Liebe* for women and *Lieber* for men."),
  ("Mit freundlichen Grüßen","Formal closing, then your full name."),
  ("Viele Grüße / Liebe Grüße / Bis bald","Informal closing. Never mix: *Sehr geehrte ...* goes with *Mit freundlichen Grüßen*.")],
 "task":"Write the greeting and closing for (a) an email to your landlord Herr Becker and (b) a message to your friend Lena.",
 "model":"(a) Sehr geehrter Herr Becker, ... Mit freundlichen Grüßen, Ihr Name.\n(b) Liebe Lena, ... Viele Grüße, dein Name."},
{"id":"f2","sec":"schreiben","title":"Starting the email (reason for writing)","when":"First sentence after the greeting. It shows the reader at once what your email is about.",
 "items":[("ich schreibe Ihnen, weil ich eine Frage zu ... habe.","*weil* sends the verb to the end: *habe*."),
  ("ich möchte mich für ... bedanken.","*sich bedanken für + Akkusativ*."),
  ("vielen Dank für Ihre / deine E-Mail.","*für* + accusative: *Ihre E-Mail* (feminine)."),
  ("ich schreibe Ihnen wegen ...","*wegen* + noun. Short and useful."),
  ("ich habe Ihre Anzeige gelesen und interessiere mich für ...","*sich interessieren für + Akkusativ*.")],
 "task":"Write one opening sentence for each: (a) you want to ask a landlord about a flat, (b) you thank a colleague for a birthday invitation.",
 "model":"(a) ich schreibe Ihnen wegen der Wohnung in der Hauptstraße.\n(b) vielen Dank für deine Einladung zu deinem Geburtstag."},
{"id":"f3","sec":"schreiben","title":"Polite requests and questions","when":"Leitpunkte often say: *bitten Sie um ...* or *fragen Sie nach ...*. Use Konjunktiv II to sound polite.",
 "items":[("Könnten Sie mir bitte ... schicken?","*könnten* is Konjunktiv II of können. The infinitive goes at the end."),
  ("Ich wäre Ihnen dankbar, wenn Sie mir ... mitteilen könnten.","Very formal. The *wenn* clause has the verbs at the end."),
  ("Ich möchte gern wissen, ob ... möglich ist.","*ob* = indirect yes/no question, verb at the end."),
  ("Wissen Sie, wann / wo / wie ...?","Indirect question with a W-word: verb at the end."),
  ("Dürfte ich Sie bitten, ... zu ...?","Very polite. *zu* + infinitive at the end: *Dürfte ich Sie bitten, mir zu helfen?*")],
 "task":"Write two sentences: (a) ask politely for the price of a course, (b) ask when the office is open.",
 "model":"(a) Könnten Sie mir bitte mitteilen, was der Kurs kostet?\n(b) Ich möchte gern wissen, wann das Büro geöffnet ist."},
{"id":"f4","sec":"schreiben","title":"Reasons, results and contrasts","when":"Showing you can link ideas lifts the grade for Kommunikative Gestaltung.",
 "items":[("..., weil ich krank bin.","Reason, **weil** + verb at the end."),
  ("..., denn ich bin krank.","Reason, **denn** + normal verb position. Short and informal."),
  ("..., deshalb kann ich nicht kommen.","Result, **deshalb** + verb in second place after it."),
  ("..., aber ich habe keine Zeit.","Contrast, **aber** stands outside the clause, verb order does not change."),
  ("Obwohl ich müde bin, komme ich.","**obwohl** = although. The verb goes to the end, then the main clause starts with the verb.")],
 "task":"Combine: *Ich komme nicht. Ich bin krank.* in three ways (weil, denn, deshalb).",
 "model":"Ich komme nicht, weil ich krank bin.\nIch komme nicht, denn ich bin krank.\nIch bin krank, deshalb komme ich nicht."},
{"id":"f5","sec":"schreiben","title":"Suggesting a date and ending","when":"Typical last Leitpunkt: propose a meeting, ask for an answer.",
 "items":[("Ich schlage vor, dass wir uns am Samstag um 15 Uhr treffen.","*vorschlagen, dass* + verb at the end."),
  ("Wie wäre es am Freitag?","*wäre* is Konjunktiv II. A relaxed suggestion."),
  ("Passt Ihnen / dir der Termin?","*passen + Dativ*: Ihnen / dir."),
  ("Ich freue mich auf Ihre Antwort.","*sich freuen auf + Akkusativ* (a future event)."),
  ("Über eine schnelle Antwort würde ich mich freuen.","*sich freuen über + Akkusativ*. *über* + noun to open the sentence, *würde* in second place.")],
 "task":"Propose a meeting on Saturday at 10 and ask for an answer, in two sentences.",
 "model":"Ich schlage vor, dass wir uns am Samstag um 10 Uhr treffen. Ich freue mich auf deine Antwort."},
{"id":"s1","sec":"sprechen","title":"Teil 1: introducing yourself","when":"Teil 1 is the warm-up (15 points). A calm, complete introduction gives easy points.",
 "items":[("Ich heiße ... und komme aus ...","Start simple. *kommen aus + Dativ*."),
  ("Ich wohne seit ... Jahren in ...","*seit* + dative plural, -n on the noun."),
  ("Ich arbeite als ... bei ...","*arbeiten als + job without article*."),
  ("In meiner Freizeit ... ich gern ...","The verb is in second place after the opener."),
  ("Meine Familie besteht aus ...","*bestehen aus + Dativ*.")],
 "task":"Say five sentences about yourself out loud, using ich heiße, wohne seit, arbeite als, in meiner Freizeit, besteht aus.",
 "model":"Ich heiße Manu und komme aus Indien. Ich wohne seit drei Jahren in Aachen. Ich arbeite als Ingenieur bei einer Firma. In meiner Freizeit lerne ich gern Deutsch. Meine Familie besteht aus meiner Frau und mir."},
{"id":"s2","sec":"sprechen","title":"Teil 2: talking about a topic","when":"A short talk (30 points). Use a clear structure so the listeners can follow you.",
 "items":[("Ich möchte über das Thema ... sprechen.","Opening. *sprechen über + Akkusativ*."),
  ("Zuerst / Dann / Außerdem / Zum Schluss ...","Sequence words. After them the verb is in second place."),
  ("Ich finde, dass ...  /  Meiner Meinung nach ...","Opinion. *dass* sends the verb to the end. *Meiner Meinung nach* is a fixed phrase, verb follows."),
  ("Ein Beispiel dafür ist ...","Gives you a place to add an example and earns Aufgabenbewältigung points."),
  ("Das war meine Präsentation. Haben Sie Fragen?","Fixed closing. Always end with it.")],
 "task":"Talk for about one minute on 'Learning German in Germany' using the five frames in order. Say it aloud.",
 "model":"Ich möchte über das Thema Deutschlernen in Deutschland sprechen. Zuerst ... Außerdem ... Ich finde, dass man im Alltag schnell lernt. Ein Beispiel dafür ist der Supermarkt. Das war meine Präsentation. Haben Sie Fragen?"},
{"id":"s3","sec":"sprechen","title":"Teil 3: planning together","when":"A dialogue (30 points). You must react to your partner: agree, disagree, compromise.",
 "items":[("Ich schlage vor, dass wir ...","Suggesting. *dass* + verb at the end."),
  ("Wie wäre es, wenn wir ...?","Soft suggestion, Konjunktiv II."),
  ("Das finde ich gut. / Da stimme ich dir zu.","Agree. *zustimmen + Dativ*: *dir, Ihnen*."),
  ("Ich bin nicht sicher, ob das passt, weil ...","Polite doubt with a reason. *ob* and *weil* clauses both end with the verb."),
  ("Dann machen wir es so: ...","Closing the decision, the verb is in second place.")],
 "task":"You plan a birthday party with a friend. Say: a suggestion, an agreement, a doubt with reason and a final decision.",
 "model":"Ich schlage vor, dass wir im Park feiern. Das finde ich gut. Ich bin nicht sicher, ob das passt, weil es regnen kann. Dann machen wir es so: Wir feiern im Park und haben ein Zelt dabei."}]
def fr(f):
    return {"id":f["id"],"sec":f["sec"],"title":f["title"],"when":f["when"],"task":f["task"],"model":f["model"],"items":[{"de":a,"en":b} for a,b in f["items"]]}
out={"gaps1":G1,"gaps2":G2,"fix":[ff(x) for x in FIX],"frames":[fr(f) for f in FR]}
# sanity checks
for g in G1:
    assert g["text"].count("{")==len(g["gaps"]),g["id"]
    for x in g["gaps"]:assert len(x["o"])==3
for g in G2:
    assert g["text"].count("{")==len(g["gaps"]),g["id"]
    for x in g["gaps"]:assert x["ok"] in g["box"]
for x in out["fix"]:assert sum(o["ok"] for o in x["o"])==1,x["wrong"]
os.makedirs("docs/playground",exist_ok=True)
json.dump(out,open("docs/playground/bank-lernen.json","w",encoding="utf8"),ensure_ascii=False,separators=(",",":"))
print("ok",len(G1),len(G2),len(FIX),len(FR))
