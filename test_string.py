from gensim.summarization import summarize
from app.mcq_generation import MCQGenerator
MCQ_Generator = MCQGenerator(True)


def summarize_pdf(text_1, ratio=0.2):
    summary_1 = summarize(text_1, ratio=ratio)
    return summary_1


# Example usage:
text = """
One can talk endlessly about Mothers. For several weeks enemy hosts had
surrounded the city in a tight ring of steel; by night fires were lit and the flames peered
through the inky blackness at the walls of the city like a myriad red eyes—they blazed
malevolently, and their menacing glare evoked gloomy thoughts within the beleaguered
city.
From the walls they saw the enemy noose draw tighter; saw the dark shadows
hovering about the fires, and heard the neighing of well-fed horses, the clanging of
weapons, the loud laughter and singing of man confident of victory—and what can be
more jarring to the ear than the songs and laughter of the enemy?
The enemy had thrown corpses into all the streams that fed water to the city,
they had burned down the vineyards around the walls, trampled the fields, cut down the
orchards—the city was now exposed on all sides, and nearly every day the cannon and
muskets of the enemy showered it with lead and iron.
Detachments of war-weary, half-starved soldiers trooped sullenly through the
narrow streets of the city; from the windows of houses issued the groans of the
wounded, the cries of the delirious, the prayers of women and the wailing of children.
People spoke in whispers, breaking off in the middle of a sentence, tensely alert; was
not that the enemy advancing?
Worst of all were the nights; in the nocturnal stillness the groans and cries were
more distinctly audible; black shadows crept stealthily from the gorges of the distant
mountains towards the half-demolished walls, hiding the enemy camp from view, and
over the black ridges of the mountains rose the moon like a lost shield dented by sword
blows.
And the people in the city, despairing of succour, worn out by toil and hunger,
their hope of salvation waning from day to day, the people in the city stared in horror at
that moon, at the sharp-toothed ridges of the mountains, the black mass of the gorges
and the noisy camp of the enemy. Everything spoke to them of death, and not a star was
there in the sky to give them consolation.
They were afraid to light the lamps in the houses, and a heavy darkness
enveloped the streets, and in this darkness, like a fish stirring in the depths of a river, a
woman draped from head to foot in a black cloak moved soundlessly.
When they saw her, people whispered to one another:
'Is it she?'
'It is she!'
 49
And they withdrew into the niches under archways, or hurried past her with
lowered heads. The patrol chiefs warned her sternly:
'Abroad again, Monna Marianna? Take care, you may be killed and nobody will
bother to search for the culprit...'
She drew herself up and stood waiting, but the patrols passed by, either not
daring or else scorning to raise their hand against her; the armed men avoided her like a
corpse and, left alone in the darkness, she continued her solitary wanderings from street
to street, soundless and black like the incarnation of the city's misfortune, while all
about her, as though pursuing her, melancholy sounds issued from the night; the groans,
cries, prayers and the sullen murmur of soldiers who had lost all hope of victory.
A citizen and a mother, she thought of her son and her country; for at the head
of the men who were destroying her town was her son, her gay, handsome, heartless
son. Yet, not so long ago she had looked upon him with pride regarding him as her
precious gift to her country, a beneficent force she had brought forth to aid the people
of the city where she herself had been born and reared. Her heart was bound by
hundreds of invisible threads to these ancient stones with which her forefathers had
built their homes and raised the walls of the city; to the soil wherein lay buried the
bones of her kinsfolk, to the legends, the songs and the hopes of the people. And now
this heart had lost a loved one and it wept. She weighed in her heart as on scales her
love for her son and her love for her native city, and she could not tell which weighed
the more.
And so she wandered thus by night through the streets and many, failing to
recognise her, drew back in fear mistaking her black figure for the incarnation of Death
that was so near to all of them, and when they did recognise her, they turned silently
away from the mother of a traitor.
But one day in a remote corner by the city walls she saw another woman,
kneeling beside a corpse, so still that she seemed part of the earth. The woman was
praying, her grief-stricken face upturned to the stars. And on the wall overhead the
sentries spoke in low tones their weapons grating against the stone.
The traitor's mother asked:
'Your husband?'
'No.'
'Your brother?'
'My son. My husband was killed thirteen days ago, my son today.'
And rising from her knees, the mother of the slain man said humbly:
'The Madonna sees all and knows all, and I am grateful to her!' 'For what?'
asked the first, and the other replied: 'Now that he has died honourably fighting for his
country I can say that I feared for him: he was light-hearted, too fond of revelry and I
 50
feared that he might betray his city, as did the son of Marianna, the enemy of God and
Man, the leader of our foes, may he be so cursed and the womb that bore him!'
Marianna covered her face and went on her way. The next morning she
appeared before the city's defenders and said:
'My son has come to be your enemy. Either kill me or open the gates that I may
go to him...'
They replied:
'You are a human being, and your country must be precious to you; your son is
as much an enemy to you as to each one of us.'
I am his mother. I love him and feel that I am to blame for what he has become!'
Then they took counsel with one another and decided.
'It would not be honourable to kill you for the sins of your son. We know that
you could not have led him to commit this terrible sin, and we can understand your
distress. But the city does not need you even as a hostage; your son cares nought for
you, we believe that he has forgotten you, fiend that he is, and there is your punishment
if you think you have deserved it! We believe that is more terrible than death itself!'
'Yes,' she said. 'It is indeed more terrible.'
And so they opened the gates and suffered her to leave the city and watched
long from the battlements as she departed from her native soil, now drenched with the
blood her son had spilt. She walked slowly, for her feet were reluctant to tear
themselves away from this soil, and she bowed to the corpses of the city's defenders,
kicking aside a broken weapon in disgust, for all weapons are abhorrent to mothers save
those that protect life.
She walked as though she carried a precious phial of water beneath her cloak
and feared to spill a drop and as her figure grew smaller and smaller to those who
watched from the city wall, it seemed to them that with her went their dejection and
hopelessness.
They saw her pause halfway and throwing back the hood of her cloak turn back
and gaze long at the city. And over in the enemy's camp they saw her alone. They
approached and inquired who she was and whence she had come.
'Your leader is my son,' she said, and not one of the soldiers doubted it. They
fell in beside her, singing his praises, saying how clever and brave he was, and she
listened to them with head proudly raised, showing no surprise, for her son could not be
otherwise.
 51
And now, at last, she stood before him whom she had known nine months
before his birth, him whom she had never felt apart from her own heart. In silk and
velvet he stood before her, his weapons studded with precious stones. All was as it
should be, thus had she seen him so many times in her dreams rich, famous and
admired.
'Mother!' he said, kissing her hands. 'Thou hast come to me, thou art with me,
and tomorrow I shall capture that accursed city!'
Intoxicated with his prowess, crazed with the thirst for more glory, he answered
her with the arrogant heat of youth:
'I was born into the world and for the world, and I mean to make the world
quake with wonder of me! I have spared this city for thy sake, it has been like a thorn in
my flesh and has retarded my swift rise to fame. But now tomorrow I shall smash that
nest of obstinate fools!'
'Where every stone knows and remembers them as a child,' she said.
'Stones are dumb unless man makes them speak. Let the mountains speak of me,
that is what I wish!' 'And what of men?' she asked.
'Ah yes, I have not forgotten them, Mother. I need them too, for only in men's
memory are heroes immortal!'
She said: 'A hero is he who creates life in defiance of death, who conquers death
...’
'No!' he objected. 'The destroyer is as glorious as the builder of a city. See, we
do not know who it was that built Rome-Aeneas or Romulus—yet we know well the
name of Alaric and the other heroes who destroyed the city . . . '
'Which outlived all names.' the mother reminded him.
Thus they conversed until the sun sank to rest; less and less frequently did she
interrupt his wild speech, lower sank her proud head.
A Mother creates, she protects, and to speak to her of destruction means to
speak against her; but he did not know this, he did not know that he was negating her
reason for existence.
A Mother is always opposed to death; the hand that brings death into the house
of men is hateful and abhorrent to Mothers. But the son did not perceive this, for he was
blinded by the cold glitter of glory that deadens the heart.
Nor did he know that a Mother can be as clever and ruthless as she is fearless,
when the life she creates and cherishes is in question.
 52
She sat with bowed head, and through the opening in the leader's richly
appointed tent she saw the city where first she had felt the sweet tremor of life within
her and the anguished convulsions of the birth of this child who now thirsted for
destruction.
The crimson rays of the sun dyed the walls and towers of the city blood-red,
cast a baleful glare on the windowpanes so that the whole city seemed to be a mass of
wounds with the crimson sap of life flowing from each gash. Presently the city turned
black as a corpse and the stars shone above it life funeral candles.
She saw the dark houses where people feared to light candles so as not to attract
the attention of the enemy, saw the streets steeped in gloom and rank with the stench of
corpses, heard the muffled whispers of people awaiting death—she saw it all, all that
was near and dear to her stood before her, dumbly awaiting her decision, and she felt
herself the mother of all those people in her city.
Clouds descended from the black peaks into the valley and swooped down like
winged steeds upon the doomed city.
'We may attack tonight,' said her son, 'if the night is dark enough! It is hard to
kill when the sun shines in your eyes and the glitter of the weapons blinds you, many a
blow goes awry,' he remarked, examining his sword.
The mother said to him: 'Come, my son, lay thy head on my breast and rest,
remember how gay and kind thou wert as a child, and how everyone loved thee. . . '
He obeyed her, laid his head in her lap and closed his eyes, saying:
‘I love only glory and I love thee for having made me as I am.'
'And dost thou not desire children?' she asked finally.
'What for? That they might be killed? Someone like me will kill them; that will
give me pain and I shall be too old and feeble to avenge them.'
'Thou art handsome, but as barren as a streak of lightning,' she said with a sigh.
'Yes, like lightning. . .' he replied, smiling.
And he dozed there on his mother's breast like a child.
Then, covering him with her black cloak, she plunged a knife into his heart, and
with a shudder he died, for who knew better than she where her son's heart beat. And,
throwing his corpse at the feet of the astonished sentries, she said addressing the city:
'As a Citizen, I have done for my country all 1 could: as a Mother I remain with
my son! It is too late for me to bear another; my life is of no use to anyone.'
 53
And the knife, still warm with his blood, her blood, she plunged with a firm
hand into her own breast, and again she struck true, for an aching heart is not hard to
find. 

"""
summary = summarize_pdf(text, 0.3)
questions = MCQ_Generator.generate_mcq_questions(summary, 10)
print(summary)
