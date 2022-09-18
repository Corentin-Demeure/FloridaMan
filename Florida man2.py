from random import randint

with open('adjective.txt') as f:
    adjective = [line.rstrip() for line in f]
with open('adverb.txt') as f:
    adverb = [line.rstrip() for line in f]
with open('epithete.txt') as f:
    epithete = [line.rstrip() for line in f]
with open('epithete_after.txt') as f:
    epithete_after = [line.rstrip() for line in f]
with open('location.txt') as f:
    location = [line.rstrip() for line in f]
with open('noun.txt') as f:
    noun = [line.rstrip() for line in f]
with open('part 2.txt') as f:
    part2 = [line.rstrip() for line in f]
with open('verb1 b4 ing.txt') as f:
    verb1_b4_ing = [line.rstrip() for line in f]
with open('verb1 b4 to.txt') as f:
    verb1_b4_to = [line.rstrip() for line in f]
#convert the text 'verb:particle' into a list of list ['verb', 'particle']
with open('verb2.txt') as f:
    temporary_lst = []
    for line in f:
        if line.count(':') == 2:
            temporary_lst.append(line.rstrip())
        elif line.count(':') == 1:
            temporary_lst.append(line.rstrip() + ':')
        elif line.count(':') == 0:
            temporary_lst.append(line.rstrip() + '::')
    verb2 = [line.split(':') for line in temporary_lst]

def adjectiveF():
    if randint(0, 3) == 0:
        list.append(adjective[randint(0, len(adjective)-1)])

def adverbF():
    if randint(0, 3) == 0:
        list.append(adverb[randint(0, len(adverb)-1)])

def epitheteF():
    if randint(0, 10) == 0:
        list.append(epithete[randint(0, len(epithete)-1)])

def epithete_afterF():
    if randint(0, 10) == 0:
        list.append(epithete_after[randint(0, len(epithete_after) - 1)])

def locationF():
    if randint(0, 1):
        list.append(location[randint(0, len(location)-1)])

def nounF():
    list.append(noun[randint(0, len(noun)-1)])
    #the post-noun particle must remain at the end of nounF because it goes after the noun
    if not verb2[particle_verb_index][2] == '':
        list.append(verb2[particle_verb_index][2])

def part2F():
    if randint(0, 1):
        list.append(part2[randint(0, len(part2)-1)])

def verb1F():
    global toing

    if randint(0, 3) == 0:
        if randint(0, 5) == 0:
            list.append(verb1_b4_to[randint(0, len(verb1_b4_to)-1)])
            toing = 'to'
        else:
            list.append(verb1_b4_ing[randint(0, len(verb1_b4_ing)-1)])
            toing = 'ing'
    else:
        toing = '3S'

def verb2F():
    global particle_verb_index
    particle_verb_index = (randint(0, len(verb2)-1))
    list.append(verb2[particle_verb_index][0])

    if toing == 'ing':
        #does the word end in e?
        if list[-1][-1] == 'e': #yes
            #keep the entire word but the last letter which is a e
            list[-1] = list[-1][:-1]

        else: #no
            # repeat twice final consonant of last word in list if ending pattern is consonant-vowel-consonant and final consonant is not vwxjyh
            if not list[-1][-3] in 'aeiou' and list[-1][-2] in 'aeiou' and not list[-1][-1] in 'vwxjyh':
                list[-1] += list[-1][-1]
        list[-1] += 'ing'

    elif toing == '3S':
        if list[-1] == 'have':
            list[-1] = 'has'
        elif list[-1][-2:] in 'ch, sh, ss' or list[-1][-1] == 'o':
            list[-1] += 'es'
        elif list[-1][-1] == 'y' and list[-1][-2] not in 'aeiou':
            # he fly => he flies
            list[-1] = list[-1][:-1] + 'ies'
        else:
            list[-1] += 's'

    # This script adds the pre-noun particle after everything verb2-related
    # the pre-noun particle must remain at the end of verb2F because it goes after the verb2
    if not verb2[particle_verb_index][1] == '':
        list.append(verb2[particle_verb_index][1])


list = []
epitheteF()
list.append('Florida')
if randint(0, 4) == 0:
    list.append('woman')
else:
    list.append('man')
epithete_afterF()
verb1F()
adverbF()
verb2F()
adjectiveF()
nounF()
locationF()
part2F()

final_string = ''
for item in list:
    #makes sure the first word of string doesn't begin with a space
    #makes sure there is no space between a noun and a comma/period/single quote (Plane's object instead of Plane 's object)
    if item == list[0] or item[0] in "',.":
        final_string += item
    else:
        final_string += ' ' + item
print(final_string)