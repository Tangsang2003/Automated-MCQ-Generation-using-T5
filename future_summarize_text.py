import nltk
from textwrap3 import wrap
from transformers import T5ForConditionalGeneration, T5Tokenizer
from nltk.tokenize import sent_tokenize
summary_model = T5ForConditionalGeneration.from_pretrained('t5-base')
summary_tokenizer = T5Tokenizer.from_pretrained('t5-base')


def postprocesstext (content):
  final=""
  for sent in sent_tokenize(content):
    sent = sent.capitalize()
    final = final +" "+sent
  return final


def summarizer(text,model,tokenizer):
  text = text.strip().replace("\n"," ")
  text = "summarize: "+text
  # print (text)
  max_len = 512
  encoding = tokenizer.encode_plus(text,max_length=max_len, pad_to_max_length=False,truncation=True, return_tensors="pt")

  input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

  outs = model.generate(input_ids=input_ids,
                                  attention_mask=attention_mask,
                                  early_stopping=True,
                                  num_beams=3,
                                  num_return_sequences=1,
                                  no_repeat_ngram_size=2,
                                  min_length = 75,
                                  max_length=300)


  dec = [tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]
  summary = dec[0]
  summary = postprocesstext(summary)
  summary= summary.strip()

  return summary

text = """
Paul Michael Levesque (born July 27, 1969), better known by the ring name Triple H, is an American business executive, actor, and retired professional wrestler. Regarded as one of the greatest professional wrestlers of all time, he currently serves as the chief content officer and head of creative for WWE.

Born and raised in Nashua, New Hampshire, Levesque began his wrestling career in 1992 with the International Wrestling Federation (IWF) under the ring name Terra Ryzing. He joined World Championship Wrestling (WCW) in 1994 and was soon repackaged as a French-Canadian aristocrat named Jean-Paul Lévesque. In 1995, he signed with the World Wrestling Federation (WWF, now WWE) and became better known as Hunter Hearst Helmsley, which was later shortened to Triple H.[5] In WWF, Triple H gained industry fame as a member of The Kliq and co-founding the influential D-Generation X (DX) stable, which became a major element of the "Attitude Era" in the 1990s. After winning his first WWF Championship in 1999, he became a fixture of the company's main event scene,[4][6] and was widely regarded as one of the best wrestlers in North America by the turn of the millennium.[7] Triple H has headlined several major WWE pay-per-view events, closing the company's flagship annual event, WrestleMania, on seven occasions.[a]

Triple H won a number of championships in his career, being a five-time Intercontinental Champion, a three-time world tag team champion (two World Tag Team Championship reigns, and one Unified WWE Tag Team Championship reign), a two-time European Champion, and a 14-time world champion, making him the company's seventh Triple Crown Champion and second Grand Slam Champion. He is also a two-time Royal Rumble match winner, and a King of the Ring tournament winner.[8][9] Triple H gained late-career praise for his behind-the-scenes work at WWE, creating the developmental branch NXT and earning acknowledgment for his business acumen in professional wrestling.[10]

Outside of wrestling, Triple H has received media attention due to his marriage to Stephanie McMahon, daughter of WWE chairman Vince McMahon.[11] In 2019, he was inducted into the WWE Hall of Fame as part of D-Generation X.[12] After suffering from heart failure in September 2021 that resulted in a 15-hour surgery and required the implementation of an ICD, Triple H officially retired from in-ring competition in April 2022.[13]

Early life
Paul Michael Levesque was born in Nashua, New Hampshire, on July 27, 1969.[14] He has a sister named Lynn.[15] His first experience of watching professional wrestling was seeing a match involving Chief Jay Strongbow as a young child.[16] He attended Nashua High School, where he played baseball and basketball.[17] Following his graduation in 1987, Levesque continued to enter bodybuilding competitions—having taken up bodybuilding at the age of 14 because he wanted to look like professional wrestlers—and won the 1988 Mr. Teenage New Hampshire competition at the age of 19.[18][15] While working as a manager of a gym in Nashua, he was introduced to world champion powerlifter Ted Arcidi, who was employed by WWE at the time. Eventually, after numerous attempts, Levesque persuaded Arcidi to introduce him to former wrestler Killer Kowalski, who ran a professional wrestling school in Malden, Massachusetts.[16][19]

Professional wrestling career
Training and early career (1990–1993)
In early 1990, Levesque began to train as a professional wrestler at Killer Kowalski's school in Malden.[4][17] His classmates included fellow future WWF wrestlers Chyna and Perry Saturn. He made his professional debut on March 24, 1992, in Kowalski's promotion, the International Wrestling Federation (IWF), under the name "Terra Ryzing", defeating Tony Roy.[20] In July 1992, he defeated Mad Dog Richard to win the IWF Heavyweight Championship.[1] Managed by John Rodeo, he wrestled for various promotions on the East Coast independent circuit until 1993.[21]

World Championship Wrestling (1994–1995)
In early 1994, Levesque signed a one-year contract with World Championship Wrestling (WCW).[15][22] In his first televised match, Levesque debuted as a villain named Terror Risin', defeating Keith Cole. His ring name was soon modified to Terra Ryzing, which he used until mid-1994, when he was renamed Jean-Paul Lévesque.[5][23] This gimmick referred to his surname's French origins and he was asked to speak with a French accent, as he could not speak French.[24] During this time, he began using his finishing maneuver, the Pedigree.[16]

Levesque had a brief feud with Alex Wright that ended on December 27 at Starrcade[5] with Wright pinning him.[25] Between late 1994 and early 1995, Lévesque briefly teamed with Lord Steven Regal, whose upper class British persona was similar to Lévesque's character.[23] The team was short-lived, however, as Levesque left for the World Wrestling Federation (WWF) in January 1995 after WCW and Levesque could not come to terms on a new contract.[16][non-primary source needed]

World Wrestling Federation/Entertainment/WWE (1995–present)
Intercontinental Champion (1995–1997)

Helmsley wore a tailcoat suit and carried a traditional atomizer perfume bottle to highlight his extreme snobbishness.
In a modified version of his gimmick in WCW, Levesque started his WWF career as a "Connecticut Blueblood".[24] According to Levesque, J. J. Dillon originally gave him the name of Reginald DuPont Helmsley, but Levesque asked for a name to play with the first letters and management ultimately agreed to his suggestion of Hunter Hearst Helmsley.[26] He appeared in taped vignettes, in which he talked about how to use proper etiquette, up until his wrestling debut on the April 30, 1995 episode of Wrestling Challenge defeating Buck Zumhofe.[27] Helmsley made his WWF pay-per-view debut on August 27 at SummerSlam, defeating Bob Holly.[28] Helmsley remained undefeated during the early months of his career, suffering his first pinfall at the hands of The Undertaker in a Survivor Series match at the namesake event. In the fall of 1995, Helmsley began a feud with the hog farmer Henry O. Godwinn, culminating in an infamous Hog Pen match on December 17 at In Your House 5: Seasons Beatings, where Helmsley was victorious.[29]
"""
summarized_text = summarizer(text,summary_model,summary_tokenizer)


print ("\noriginal Text >>")
for wrp in wrap(text, 150):
  print (wrp)
print ("\n")
print ("Summarized Text >>")
for wrp in wrap(summarized_text, 150):
  print (wrp)
print ("\n")