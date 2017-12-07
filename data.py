# import libraries
import nltk

data = [
    ('The defendant has a leadership role within VW, federal officials said.', 'neutral'),
    ('The UKs spending watchdog has called the project risky and expensive.', 'negative'),
    ('The Initiative on Global Markets panel of economic experts was recently asked about the Republican tax plan.', 'neutral'),
    ('GWR unveiled its new trains in October, with up to two hanging bike storage spaces per carriage.', 'positive'),
    ('In the days of London smogs it was possible to both see pollution and smell it.', 'negative'),
    ('There was a sense of disbelief that I had been so close, a clumsy intruder among this wild tangle of trees.', 'negative'),
    ('And one by one, each of the big four Australian banks ruled out financing the mine.', 'positive'),
    ('Fusion power is one of the most sought-after technological goals in the pursuit of clean energy.', 'positive'),
    ('It is arguing that the switch to electric transport will drive up future demand.', 'positive'),
    ('Theres a lot of eyes on Antarctica right now and a lot of scientists want to know whats going to happen.', 'negative'),
    ('Winter riding in rural areas can be more tricky, but even modern lights can make it much easier.', 'positive'),
    ('Chung said traffic pollution might also affect younger people doing their shopping in the heart of a city.', 'negative'),
    ('Food sustainability map Crossley said this highlighted the challenge facing the UK as Brexit approached.', 'negative'),
    ('North Alaska is the countrys last frontier, and hes letting the oil industry suck the life out of it.', 'negative'),
    ('What the report also shows is that the biggest uncertainty in future climate change is us.', 'negative'),
    ('The 2015 Paris Accord recognised the contribution of indigenous knowledge in dealing with climate change.', 'positive'),
    ('No society can afford to ignore air pollution.', 'negative'),
    ('In the Facebook ad the car was described as a clean car and helps to give back to the environment.', 'positive'),
    ('Ask How could the UK deal with plastic waste without exporting it?', 'neutral'),
    ('Alberto Bai, a Matsés traditional healer, in the healing forest near Buenas Lomas Nueva in Perus Amazon.', 'neutral'),
    ('Liberating the earth means defending the land, says José Rene Guetio, a Nasa elder.', 'positive'),
    ('Will Norman is Londons walking and cycling commissioner', 'neutral'),
    ('Because polar bears rely on sea ice to hunt seals, global warming also threatens their species.', 'negative'),
    ('The US Global Change Research Program recently released a Climate Science Special Report.', 'neutral'),
    ('The first main chapter deals with changes to the climate and focuses much attention on global temperatures.', 'neutral'),
    ('No society can afford to ignore air pollution.', 'negative'),
    ('The Luxembourg-based court of justice of the European Union is the highest court in Europe.', 'neutral'),
    ('Brexit makes the headlines every day without fail, even when nothing has happened.', 'negative'),
    ('They should not allow the popularity of the term populism to mask the nativism of the radical right.', 'negative'),
    ('In November, Momentum said it had spent £38,743 on the general election campaign.', 'neutral'),
    ('Quiet meetings on Brexit took place between civil servants in Ireland and Northern Ireland.', 'neutral'),
    ('By 2016, David Camerons austerity agenda had seen child poverty rates shoot up to 30%.', 'negative'),
    ('The DUP leader also sought to repair some of the damaged relations with the Irish government on Wednesday.', 'neutral'),
    ('There is a risk that a Tories versus the police row will have a domino effect on her cabinet.', 'negative'),
    ('Britains exit from the EU  taking Northern Ireland with it  risks a return to a hard or policed border.', 'negative'),
    ('Yet rather than stay shoulder to shoulder with the Union, the British chose to be on their own again.', 'negative'),
    ('‘The Tories economic strategy failed on its own stated terms.', 'negative'),
    ('Adonis criticised Johnson on Twitter for failing to speak out against high pay packets.', 'negative'),
    ('Others have urged the government to ensure that EU funding is replaced from 2019 onwards.', 'neutral'),
    ('The Health and Safety Executives myth-busting website has to rebut such nonsense every week.', 'negative'),
    ('My experience of employing disabled people is that they are brilliant employees.', 'positive'),
    ('The new defence secretary told the Daily Mail: A dead terrorist cant cause any harm to Britain.', 'negative'),
    ('A meeting to discuss them was scheduled for 31 May, but the attack at Manchester Arena happened on 22 May.', 'negative'),
    ('A number of big, unanswered questons about ACOs remain, despite their imminent arrival in the NHS, he adds.', 'neutral'),
    ('London depends on foreign workers to keep growing and therefore keep boosting that tax export.', 'positive'),
    ('There were signs that progress was being made towards a deal to avoid a hard border on the island of Ireland.', 'positive'),
    ('I will also discuss with House officials the steps necessary to repay previous travel claims.', 'positive')
]


def create_training_data():
    tweets = []
    for (words, sentiment) in data:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 4]
        tweets.append((words_filtered, sentiment))
    return tweets


print(create_training_data())


training_data = [
    (['big', 'four', 'australian', 'banks', 'ruled', 'out', 'financing'], 'positive'),
    (['fusion', 'power', 'most', 'sought-after', 'technological', 'goals', 'pursuit', 'clean', 'energy'], 'positive'),
    (['arguing', 'switch', 'electric', 'transport', 'will', 'drive', 'future', 'demand'], 'positive'),
    (['theres', 'lot', 'eyes', 'antarctica', 'right', 'now', 'lot', 'scientists', 'want', 'know', 'whats', 'going', 'happen'], 'negative'),
    (['winter', 'riding', 'rural', 'areas', 'can', 'more', 'tricky,', 'but', 'even', 'modern', 'lights', 'can', 'make', 'much', 'easier'], 'positive'),
    (['chung', 'said', 'traffic', 'pollution', 'might', 'also', 'affect', 'younger', 'people', 'doing', 'their', 'shopping', 'heart', 'city'], 'negative'),
    (['food', 'sustainability', 'map', 'crossley', 'said', 'highlighted', 'challenge', 'facing', 'brexit', 'approached'], 'negative'),
    (['north', 'alaska', 'countrys', 'last', 'frontier,', 'hes', 'letting', 'oil', 'industry', 'suck', 'life', 'out', 'it'], 'negative'),
    (['what', 'report', 'also', 'shows', 'biggest', 'uncertainty', 'future', 'climate', 'change', 'us'], 'negative'),
    (['2015', 'paris', 'accord', 'recognised', 'contribution', 'indigenous', 'knowledge', 'dealing', 'with', 'climate', 'change'], 'positive'),
    (['society', 'can', 'afford', 'ignore', 'air', 'pollution'], 'negative'),
    (['facebook', 'car', 'was', 'described', 'clean', 'car', 'helps', 'give', 'back', 'environment'], 'positive'),
    (['ask', 'how', 'deal', 'with', 'plastic', 'waste', 'without', 'exporting'], 'neutral'),
    (['alberto', 'bai,', 'matsés', 'traditional', 'healer,', 'healing', 'forest', 'near', 'buenas', 'lomas', 'nueva', 'perus', 'amazon'], 'neutral'),
    (['liberating', 'earth', 'means', 'defending', 'land,', 'says', 'josé', 'rene', 'guetio,', 'nasa', 'elder'], 'positive'),
    (['will', 'norman', 'londons', 'walking', 'cycling', 'commissioner'], 'neutral'),
    (['because', 'polar', 'bears', 'rely', 'sea', 'ice', 'hunt', 'seals,', 'global', 'warming', 'also', 'threatens', 'their', 'species'], 'negative'),
    (['global', 'change', 'research', 'program', 'recently', 'released', 'climate', 'science', 'special', 'report'], 'neutral'),
    (['first', 'main', 'chapter', 'deals', 'with', 'changes', 'climate', 'focuses', 'much', 'attention', 'global', 'temperatures'], 'neutral'),
    (['society', 'can', 'afford', 'ignore', 'air', 'pollution'], 'negative'),
    (['luxembourg-based', 'court', 'justice', 'european', 'union', 'highest', 'court', 'europe'], 'neutral'),
    (['brexit', 'makes', 'headlines', 'every', 'day', 'without', 'fail,', 'even', 'when', 'nothing', 'happened'], 'negative'),
    (['they', 'should', 'not', 'allow', 'popularity', 'term', 'populism', 'mask', 'nativism', 'radical', 'right'], 'negative'),
    (['november,', 'momentum', 'said', 'spent', '£38,743', 'general', 'election', 'campaign'], 'neutral'),
    (['quiet', 'meetings', 'brexit', 'took', 'place', 'between', 'civil', 'servants', 'ireland', 'northern', 'ireland'], 'neutral'),
    (['2016,', 'david', 'camerons', 'austerity', 'agenda', 'seen', 'child', 'poverty', 'rates', 'shoot', '30%'], 'negative'),
    (['dup', 'leader', 'also', 'sought', 'repair', 'some', 'damaged', 'relations', 'with', 'irish', 'government', 'wednesday'], 'neutral'),
    (['there', 'risk', 'tories', 'versus', 'police', 'row', 'will', 'have', 'domino', 'effect', 'her', 'cabinet'], 'negative'),
    (['britains', 'exit', 'from', 'taking', 'northern', 'ireland', 'with', 'risks', 'return', 'hard', 'policed', 'border'], 'negative'),
    (['yet', 'rather', 'stay', 'shoulder', 'shoulder', 'with', 'union,', 'british', 'chose', 'their', 'own', 'again'], 'negative'),
    (['‘the', 'tories', 'economic', 'strategy', 'failed', 'its', 'own', 'stated', 'terms'], 'negative'),
    (['adonis', 'criticised', 'johnson', 'twitter', 'failing', 'speak', 'out', 'against', 'high', 'pay', 'packets'], 'negative'),
    (['others', 'have', 'urged', 'government', 'ensure', 'funding', 'replaced', 'from', '2019', 'onwards'], 'neutral'),
    (['health', 'safety', 'executives', 'myth-busting', 'website', 'rebut', 'such', 'nonsense', 'every', 'week'], 'negative'),
    (['experience', 'employing', 'disabled', 'people', 'they', 'are', 'brilliant', 'employees'], 'positive'),
    (['new', 'defence', 'secretary', 'told', 'daily', 'mail:', 'dead', 'terrorist', 'cant', 'cause', 'any', 'harm', 'britain'], 'negative'),
    (['meeting', 'discuss', 'them', 'was', 'scheduled', 'may,', 'but', 'attack', 'manchester', 'arena', 'happened', 'may'], 'negative'),
    (['number', 'big,', 'unanswered', 'questons', 'about', 'acos', 'remain,', 'despite', 'their', 'imminent', 'arrival', 'nhs,', 'adds'], 'neutral'),
    (['london', 'depends', 'foreign', 'workers', 'keep', 'growing', 'therefore', 'keep', 'boosting', 'tax', 'export'], 'positive'),
    (['there', 'were', 'signs', 'progress', 'was', 'being', 'made', 'towards', 'deal', 'avoid', 'hard', 'border', 'island', 'ireland'], 'positive'),
    (['will', 'also', 'discuss', 'with', 'house', 'officials', 'steps', 'necessary', 'repay', 'previous', 'travel', 'claims'], 'positive')
]

test_data = [
    (['defendant', 'leadership', 'role', 'within', 'federal', 'officials', 'said'], 'neutral'),
    (['uks', 'spending', 'watchdog', 'called', 'project', 'risky', 'expensive'], 'negative'),
    (['initiative', 'global', 'markets', 'panel', 'economic', 'experts', 'was', 'recently', 'asked', 'about', 'republican', 'tax', 'plan'], 'neutral'),
    (['gwr', 'unveiled', 'its', 'new', 'trains', 'october,', 'with', 'two', 'hanging', 'bike', 'storage', 'spaces', 'per', 'carriage'], 'positive'),
    (['days', 'london', 'smogs', 'was', 'possible', 'both', 'see', 'pollution', 'smell'], 'negative'),
    (['there', 'was', 'sense', 'disbelief', 'been', 'close,', 'clumsy', 'intruder', 'among', 'wild', 'tangle', 'trees'], 'negative')
]


def get_words_in_tweets(data):
    all_words = []
    for (words, sentiment) in data:
      all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


word_features = get_word_features(get_words_in_tweets(training_data))

training_set = nltk.classify.apply_features(extract_features, training_data)

classifier = nltk.NaiveBayesClassifier.train(training_set)

tweet = 'There are many young people among the Matsés, but the majority dont want to know.'
print(classifier.classify(extract_features(tweet.split())))
