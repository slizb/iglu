
from snape.make_image_dataset import *
from snape.make_image_dataset import _ImageNet
from nltk.corpus import wordnet


conf = {
    "n_classes": 2,
    "n_samples": 10,
    "out_path": "./test_images/",
    "weights": [0.8, 0.2],
    "image_source": "imagenet",
    "random_seed":42
}

random_state = get_random_state(conf["random_seed"])

synsets = _ImageNet(n_classes=conf["n_classes"],
                  weights=conf["weights"],
                  n_samples=conf["n_samples"],
                  output_dir=conf["out_path"],
                  random_state=random_state).get_ilsvrc_1000_synsets()


def get_synset_labels(wnid):
    url = "http://www.image-net.org/api/text/wordnet.synset.getwords?wnid="
    url += wnid
    request = requests.get(url)
    return request.text


def get_primary_synset_label(wnid):
    labels = get_synset_labels(wnid)
    primary_label = labels.split('\n')[0].replace(' ', '_')
    return primary_label


def get_class_similarity(a_label, b_label):

    a = wordnet.synsets(a_label)[0]
    b = wordnet.synsets(b_label)[0]
    return wordnet.wup_similarity(a, b)


def get_1000_primary_labels():
    label_dict = {}
    for syn in synsets:
        print(syn)
        label = get_primary_synset_label(syn)
        label_dict[syn] = label
    return label_dict


PRIMARY_LABELS = get_1000_primary_labels()

df = pd.DataFrame(columns=['synset_A','synset_B','synset_A_label', 'synset_B_label', 'similarity'])
i = 0

for A in synsets:

    A_label = PRIMARY_LABELS[A]

    for B in synsets:
        i += 1
        print(i)

        id = '_'.join(sorted([A, B]))

        if id in df.index:
            continue

        try:

            B_label = PRIMARY_LABELS[B]
            sim_score = get_class_similarity(A_label, B_label)

            row = {'synset_A': A,
                   'synset_B': B,
                   'synset_A_label': A_label,
                   'synset_B_label': B_label,
                   'similarity': sim_score}

            df.loc[id] = pd.Series(row)

        except:
            pass


df.to_csv('similarity_scores.csv')

