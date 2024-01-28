import textwrap

from app.mcq_generation import MCQGenerator


def show_result(generated: str, answer: str, context:str, original_question: str = ''):
    
    print('Context:')

    for wrap in textwrap.wrap(context, width=120):
        print(wrap)
    print()

    print('Question:')
    print(generated)

    print('Answer:')
    print(answer)
    print('-----------------------------')


MCQ_Generator = MCQGenerator(True)

context_a = '''The koala or, inaccurately, koala bear[a] (Phascolarctos cinereus), is an arboreal herbivorous 
marsupial native to Australia. It is the only extant representative of the family Phascolarctidae and its closest
 living relatives are the wombats, which are members of the family Vombatidae. The koala is found in coastal areas
  of the mainland's eastern and southern regions, inhabiting Queensland, New South Wales, Victoria, and South 
  Australia. It is easily recognisable by its stout, tailless body and large head with round, fluffy ears and 
  large, spoon-shaped nose. The koala has a body length of 60–85 cm (24–33 in) and weighs 4–15 kg (9–33 lb). 
  Fur colour ranges from silver grey to chocolate brown. Koalas from the northern populations are typically 
  smaller and lighter in colour than their counterparts further south. These populations possibly are separate 
  subspecies, but this is disputed.'''

context_oxygen = '''Oxygen is the chemical element with the symbol O and atomic number 8. It is a member of the 
chalcogen group in the periodic table, a highly reactive nonmetal, and an oxidizing agent that readily forms 
oxides with most elements as well as with other compounds. Oxygen is Earth's most abundant element, and after 
hydrogen and helium, it is the third-most abundant element in the universe. At standard temperature and 
pressure, two atoms of the element bind to form dioxygen, a colorless and odorless diatomic gas with the 
formula O
2. Diatomic oxygen gas currently constitutes 20.95% of the Earth's atmosphere, though this has changed 
considerably over long periods of time. Oxygen makes up almost half of the Earth's crust in the form of oxides.[3]


Dioxygen provides the energy released in combustion[4] and aerobic cellular respiration,[5] and many major 
classes of organic molecules in living organisms contain oxygen atoms, such as proteins, nucleic acids, 
carbohydrates, and fats, as do the major constituent inorganic compounds of animal shells, teeth, and bone. 
Most of the mass of living organisms is oxygen as a component of water, the major constituent of lifeforms. 
Oxygen is continuously replenished in Earth's atmosphere by photosynthesis, which uses the energy of sunlight 
to produce oxygen from water and carbon dioxide. Oxygen is too chemically reactive to remain a free element 
in air without being continuously replenished by the photosynthetic action of living organisms. Another form 
(allotrope) of oxygen, ozone (O
3), strongly absorbs ultraviolet UVB radiation and the high-altitude ozone layer helps protect the biosphere 
from ultraviolet radiation. However, ozone present at the surface is a byproduct of smog and thus a pollutant.

Oxygen was isolated by Michael Sendivogius before 1604, but it is commonly believed that the element was 
discovered independently by Carl Wilhelm Scheele, in Uppsala, in 1773 or earlier, and Joseph Priestley in 
Wiltshire, in 1774. Priority is often given for Priestley because his work was published first. Priestley, 
however, called oxygen "dephlogisticated air", and did not recognize it as a chemical element. The name oxygen 
was coined in 1777 by Antoine Lavoisier, who first recognized oxygen as a chemical element and correctly 
characterized the role it plays in combustion.

Common uses of oxygen include production of steel, plastics and textiles, brazing, welding and cutting of steels 
and other metals, rocket propellant, oxygen therapy, and life support systems in aircraft, submarines, spaceflight
 and diving.'''
context_pulchowk = '''Renewable energy sources have gained significant attention in recent years due to their 
potential to mitigate the adverse effects of traditional fossil fuels on the environment. The shift towards 
renewable energy is driven by concerns over climate change, air pollution, and the finite nature of fossil fuel 
resources.

One prominent form of renewable energy is solar power. Solar panels, which harness energy from the sun, have become
 increasingly affordable and efficient. They offer a clean and sustainable alternative to traditional electricity 
 generation methods that rely on burning fossil fuels. The adoption of solar power has led to reduced greenhouse 
 gas emissions and a lower environmental impact.

Wind energy is another key player in the renewable energy sector. Wind turbines generate electricity by harnessing
 the power of the wind. As technology advances, wind farms have become more efficient and capable of producing larger amounts of clean energy. The expansion of wind energy contributes to a diversified energy portfolio and a reduced reliance on non-renewable resources.

Hydropower, derived from the energy of moving water, is a longstanding and reliable source of renewable energy. 
Dams and other water infrastructure can generate electricity without emitting greenhouse gases. While hydropower 
has proven to be effective, concerns have been raised about its environmental impact on aquatic ecosystems and local communities.

In addition to these sources, advancements in bioenergy, geothermal energy, and tidal power are further expanding 
the renewable energy landscape. Governments, businesses, and individuals worldwide are investing in these 
sustainable alternatives to address the global energy challenge.

The transition to renewable energy is not without challenges. Initial costs of installing renewable energy 
infrastructure can be high, and there are intermittency issues with certain sources like solar and wind. 
However, ongoing research and technological advancements aim to address these challenges and make renewable 
energy more accessible and reliable.

In conclusion, the adoption of renewable energy sources has the potential to revolutionize the way we generate 
power, offering a cleaner and more sustainable future. As technology continues to evolve, the environmental 
benefits of renewable energy will likely become even more pronounced, contributing to a healthier planet for 
generations to come.'''

context_lol = '''Nepal,[a] officially the Federal Democratic Republic of Nepal,[b] is a landlocked country in South Asia. It is mainly situated in the Himalayas, but also includes parts of the Indo-Gangetic Plain. It borders the Tibet Autonomous Region of China to the north, and India to the south, east, and west, while it is narrowly separated from Bangladesh by the Siliguri Corridor, and from Bhutan by the Indian state of Sikkim. Nepal has a diverse geography, including fertile plains, subalpine forested hills, and eight of the world's ten tallest mountains, including Mount Everest, the highest point on Earth. Kathmandu is the nation's capital and the largest city. Nepal is a multi-ethnic, multi-lingual, multi-religious and multi-cultural state, with Nepali as the official language.

The name "Nepal" is first recorded in texts from the Vedic period of the Indian subcontinent, the era in ancient Nepal when Hinduism was founded, the predominant religion of the country. In the middle of the first millennium BC, Gautama Buddha, the founder of Buddhism, was born in Lumbini in southern Nepal. Parts of northern Nepal were intertwined with the culture of Tibet. The centrally located Kathmandu Valley is intertwined with the culture of Indo-Aryans, and was the seat of the prosperous Newar confederacy known as Nepal Mandala. The Himalayan branch of the ancient Silk Road was dominated by the valley's traders. The cosmopolitan region developed distinct traditional art and architecture. By the 18th century, the Gorkha Kingdom achieved the unification of Nepal. The Shah dynasty established the Kingdom of Nepal and later formed an alliance with the British Empire, under its Rana dynasty of premiers. The country was never colonised but served as a buffer state between Imperial China and British India. Parliamentary democracy was introduced in 1951 but was twice suspended by Nepalese monarchs, in 1960 and 2005. The Nepalese Civil War in the 1990s and early 2000s resulted in the establishment of a secular republic in 2008, ending the world's last Hindu monarchy.

The Constitution of Nepal, adopted in 2015, affirms the country as a secular federal parliamentary republic divided into seven provinces. Nepal was admitted to the United Nations in 1955, and friendship treaties were signed with India in 1950 and China in 1960. Nepal hosts the permanent secretariat of the South Asian Association for Regional Cooperation (SAARC), of which it is a founding member. Nepal is also a member of the Non-Aligned Movement and the Bay of Bengal Initiative. The Nepalese Armed Forces are the fifth-largest in South Asia; and are notable for their Gurkha history, particularly during the world wars, and has been a significant contributor to United Nations peacekeeping operations.

Etymology
Main article: Name of Nepal

"Nēpāla" in the late Brahmi script, in the Allahabad Pillar inscription of Samudragupta (350–375 CE).[15]
Before the unification of Nepal, the Kathmandu Valley was known as Nepal.[c] The precise origin of the term Nepāl is uncertain. Nepal appears in ancient Indian literary texts dated as far back as the fourth century BC.[which?] An absolute chronology can not be established, as even the oldest texts may contain anonymous contributions dating as late as the early modern period. Academic attempts to provide a plausible theory are hindered by the lack of a complete picture of history and insufficient understanding of linguistics or relevant Indo-European and Tibeto-Burman languages.[17]

According to Hindu mythology, Nepal derives its name from an ancient Hindu sage called Ne, referred to variously as Ne Muni or Nemi. According to Pashupati Purāna, as a place protected by Ne, the country in the heart of the Himalayas came to be known as Nepāl.[18][19][d] According to Nepāl Mahātmya,[e] Nemi was charged with protection of the country by Pashupati.[20] According to Buddhist mythology, Manjushri Bodhisattva drained a primordial lake of serpents to create the Nepal valley and proclaimed that Adi-Buddha Ne would take care of the community that would settle it. As the cherished of Ne, the valley would be called Nepāl.[21] According to Gopalarājvamshāvali, the genealogy of ancient Gopala dynasty compiled c. 1380s, Nepal is named after Nepa the cowherd, the founder of the Nepali scion of the Abhiras. In this account, the cow that issued milk to the spot, at which Nepa discovered the Jyotirlinga of Pashupatināth upon investigation, was also named Ne.[17]

Norwegian indologist Christian Lassen had proposed that Nepāla was a compound of Nipa (foot of a mountain) and -ala (short suffix for alaya meaning abode), and so Nepāla meant "abode at the foot of the mountain". He considered Ne Muni to be a fabrication.[22] Indologist Sylvain Levi found Lassen's theory untenable but had no theories of his own, only suggesting that either Newara is a vulgarism of sanskritic Nepala, or Nepala is Sanskritisation of the local ethnic;[23] his view has found some support though it does not answer the question of etymology.[24][25][26][17] It has also been proposed that Nepa is a Tibeto-Burman stem consisting of Ne (cattle) and Pa (keeper), reflecting the fact that early inhabitants of the valley were Gopalas (cowherds) and Mahispalas (buffalo-herds).[17] Suniti Kumar Chatterji believed Nepal originated from Tibeto-Burman roots – Ne, of uncertain meaning (as multiple possibilities exist), and pala or bal, whose meaning is lost entirely.[27]

History
Main article: History of Nepal
Ancient Nepal
Ancient Nepal

This painting in a Laotian temple depicts a legend surrounding the birth of Gautama Buddha c. 563 BC in Lumbini, Western Nepal.

In the premises of the Changu Narayan Temple, is a stone inscription dated 464 AD, the first in Nepal since the Ashoka inscription of Lumbini (c. 250 BC).
By 55,000 years ago, the first modern humans had arrived on the Indian subcontinent from Africa, where they had earlier evolved.[28][29][30] The earliest known modern human remains in South Asia date to about 30,000 years ago.[31] The oldest discovered archaeological evidence of human settlements in Nepal dates to around the same time.[32]

After 6500 BC, evidence for the domestication of food crops and animals, construction of permanent structures, and storage of agricultural surplus appeared in Mehrgarh and other sites in what is now Balochistan.[33] These gradually developed into the Indus Valley civilisation,[34][33] the first urban culture in South Asia.[35] Prehistoric sites of palaeolithic, mesolithic and neolithic origins have been discovered in the Siwalik hills of Dang district.[36] The earliest inhabitants of modern Nepal and adjoining areas are believed to be people from the Indus Valley civilisation. It is possible that the Dravidian people whose history predates the onset of the Bronze Age in the Indian subcontinent (around 6300 BC) inhabited the area before the arrival of other ethnic groups like the Tibeto-Burmans and Indo-Aryans from across the border.[37] By 4000 BC, the Tibeto-Burmese people had reached Nepal either directly across the Himalayas from Tibet or via Myanmar and north-east India or both.[38] Stella Kramrisch (1964) mentions a substratum of a race of pre-Dravidians and Dravidians, who were in Nepal even before the Newars, who formed the majority of the ancient inhabitants of the valley of Kathmandu.[39]

By the late Vedic period, Nepal was being mentioned in various Hindu texts, such as the late Vedic Atharvaveda Pariśiṣṭa and in the post-Vedic Atharvashirsha Upanishad.[40] The Gopal Bansa was the oldest dynasty to be mentioned in various texts as the earliest rulers of the central Himalayan kingdom known by the name 'Nepal'.[41] The Gopalas were followed by Kiratas who ruled for over 16 centuries by some accounts.[42] According to the Mahabharata, the then Kirata king went to take part in the Battle of Kurukshetra. In the south-eastern region, Janakpurdham was the capital of the prosperous kingdom of Videha or Mithila, that extended down to the Ganges, and home to King Janaka and his daughter, Sita.

Around 600 BC, small kingdoms and confederations of clans arose in the southern regions of Nepal. From one of these, the Shakya polity, arose a prince who later renounced his status to lead an ascetic life, founded Buddhism, and came to be known as Gautama Buddha (traditionally dated 563–483 BC).[43] Nepal came to be established as a land of spirituality and refuge in the intervening centuries, played an important role in transmitting Buddhism to East Asia via Tibet,[44] and helped preserve Hindu and Buddhist manuscripts.

By 250 BC, the southern regions had come under the influence of the Maurya Empire. Emperor Ashoka made a pilgrimage to Lumbini and erected a pillar at Buddha's birthplace, the inscriptions on which mark the starting point for properly recorded history of Nepal.[45] Ashoka also visited the Kathmandu valley and built monuments commemorating Gautama Buddha's visit there. By the 4th century AD, much of Nepal was under the influence of the Gupta Empire.[f][46]

In the Kathmandu valley, the Kiratas were pushed eastward by the Licchavis, and the Licchavi dynasty came into power c. 400 AD. The Lichchhavis built monuments and left a series of inscriptions; Nepal's history of the period is pieced together almost entirely from them.[47][44] In 641, Songtsen Gampo of the Tibetan Empire sends Narendradeva back to Licchavi with an army and subjugates Nepal. Parts of Nepal and Licchavi was later under the direct influences of the Tibetan empire.[48] The Licchavi dynasty went into decline in the late 8th century and was followed by a Thakuri rule. Thakuri kings ruled over the country up to the middle of the 11th century AD; not much is known of this period that is often called the dark period.[49]'''

MCQ_Generator.generate_mcq_questions(context_lol, 8)
