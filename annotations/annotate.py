import xml.etree.ElementTree as et

# The subordinating conjunctions that can introduce indirect speech
subordinators = ['quod', 'quia', 'quoniam', 'quin']

# The files we are using (there are other files in the PROIEL Treebank)
file_names = ['caes-gal.xml', 'cic-att.xml', 'cic-off.xml', 'latin-nt.xml', 'pal-agr.xml', 'per-aeth.xml']

proiel_dir = '../../proiel-treebank/'

def is_infinitive(tok):
    return tok.get('part-of-speech') == 'V-' and tok.get('relation') == 'comp' and tok.get('morphology')[3] == 'n'

def is_main_verb(tok):
    return tok.get('part-of-speech') == 'V-' and tok.get('relation') == 'pred'

def is_subordinator(tok):
    return tok.get('part-of-speech') == 'G-' and tok.get('relation') == 'comp' and tok.get('form') in subordinators

def print_filenames():
    print("Files:")
    index = 0
    for file_name in file_names:
        print('\t' + str(index) + ')', file_name)
        index += 1

def print_sentence(sent, current_index, total):
    print_loc = True
    sent_str = ''
    for tok in sent.iter('token'):
        # Print the sentence number
        if print_loc:
            print(tok.get('citation-part') + ' (' + str(current_index + 1) + '/' + str(total) + ')')
            print_loc = False

        if tok.get('form') != None:
            sent_str += tok.get('form') + tok.get('presentation-after')
    print(sent_str)

def auto_process():
    total_count = 0
    for file_name in file_names:
        root = et.Element('root')
        count = 0
        etree = et.parse(proiel_dir + file_name)
        # Create a dictionary storing morphology
        morph_tags = {}
        for morph in etree.iter('morphology'):
            for field in morph.iter('field'):
                create = True
                for value in field.iter('value'):
                    if create:
                        morph_tags[field.get('tag')] = {}
                        create = False
                    morph_tags[field.get('tag')][value.get('tag')] = value.get('summary')
                morph_tags[field.get('tag')]['-'] = 'N/A' # For inapplicable values

        for sent in etree.iter('sentence'):
            already_added = False
            get_sub_info = False
            for tok in sent.iter('token'):
                if not already_added and (is_infinitive(tok) or is_subordinator(tok)):
                    already_added = True
                    count += 1
                    if is_infinitive(tok):
                        sent.set('indirect-type', 'AcI')
                    elif is_subordinator(tok):
                        sent.set('indirect-type', tok.get('form'))
                        get_sub_info = True
                    sent.set('indirect-lemma', tok.get('lemma'))
                    sent.set('indirect-tense', morph_tags['tense'][tok.get('morphology')[2]])
                    sent.set('indirect-mood', morph_tags['mood'][tok.get('morphology')[3]])
                    sent.set('indirect-voice', morph_tags['voice'][tok.get('morphology')[4]])
                    if not get_sub_info:
                        root.append(sent)
                if get_sub_info and is_main_verb(tok):
                    sent.set('indirect-lemma', tok.get('lemma'))
                    sent.set('indirect-tense', morph_tags['tense'][tok.get('morphology')[2]])
                    sent.set('indirect-mood', morph_tags['mood'][tok.get('morphology')[3]])
                    sent.set('indirect-voice', morph_tags['voice'][tok.get('morphology')[4]])
                    root.append(sent)
                    break

        with open(file_name, 'wb') as file:
            file.write(et.tostring(root))

        print(file_name + ': annotated', count, 'sentences')
        total_count += count

    print('Processed a total of', total_count, 'sentences')

def manual_process():
    print_filenames()
    file_name = file_names[int(input("Which file? "))]
    current_index = int(input('Resumption number? '))
    root = et.Element('root')
    
    # If we are resuming, re-read the already-annotaed sentences
    if current_index > 0:
        root = et.parse(file_name).getroot()

    etree = et.parse(proiel_dir + file_name)
    sents = []
    for sent in etree.iter('sentence'):
        already_added = False
        for tok in sent.iter('token'):
            if not already_added and (is_infinitive(tok) or is_subordinator(tok)):
                already_added = True
                sents.append(sent)

    for sent in sents[current_index:]:
        print_sentence(sent, current_index, len(sents))
        answer = input('Indirect speech? ')
        if answer == 'acc' or answer in subordinators:
            sent.set('indirect-type', answer)
            root.append(sent)
        elif answer == 'pause':
            print('Your resumption number is', current_index)
            break
        else:
            pass
        current_index += 1

    with open(file_name, 'wb') as file:
        file.write(et.tostring(root))

choice = input("Manual? (default = no) ")

if choice.lower() in ['y', 'yes']:
    manual_process()
else:
    auto_process()
