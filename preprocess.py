import os
import pickle

dir = '/media/ayan-yue/DATA/corpora/swb1_dialogact_annot'

data = []
for folder in os.listdir(dir):
    if folder.startswith('sw'):

        for file in os.scandir(dir + '/' + folder):
            print('\nProcessing ' + file.path + '...\n')

            with open(file.path, 'r', encoding='utf8', errors='ignore') as text:
                chunk = text.read().split('=\n')[1:]

                if chunk:
                    for line in chunk[0].split('\n'):

                        if len(line) > 2 and '@' not in line:
                            data.append(line)


s_acts = list(set([line.split()[0] for line in data if line.split()]))

print(s_acts)
print(len(s_acts))

d = {}
for s_act in s_acts:
    d[s_act] = [line.split(': ')[1] for line in data if line.split(': ') and len(line.split(': ')) > 1 and s_act + '    ' in line]

print(d['ar'])

train = []
for s_act in d:
    for line in d[s_act]:

        train.append(line)

print(train[:200])
print('\n' + str(len(train)))


with open('s_acts.pickle', 'wb') as f:
    pickle.dump(s_acts, f)

with open('d.pickle', 'wb') as f:
    pickle.dump(d, f)

with open('train.pickle', 'wb') as f:
    pickle.dump(train, f)
