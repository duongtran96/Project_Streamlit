import streamlit as st

def levenshtein_distance(source, target):
    distance = [[0]* (len(target) + 1) for _ in range(len(source)+ 1)]

    for t1 in range(len(source)+ 1):
        distance[t1][0] = t1
    
    for t2 in range(len(target) + 1):
        distance[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(source) + 1):
        for t2 in range(1, len(target) + 1):
            if (source[t1 - 1] == target[t2 - 1 ]):
                distance[t1][t2] = distance[t1 - 1][t2 - 2]
            else:
                a = distance[t1][t2 - 1]
                b = distance[t1 - 1][t2]
                c = distance[t1- 1][t2 - 2]

                if ( a<=  b  and a <= c):
                    distance[t1][t2] = a + 1
                elif ( b <=a and b <= c):
                    distance[t1][t2] = b + 1
                else:
                    distance[t1][t2] = c + 1
    
    return distance[len(source)][len(target)]

def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words

vocabs = load_vocab(file_path = r"D:\AIO2024\Project_Module_1\Project_Streamlit\Data\vocab.txt")

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Word: ")

    if st.button('Compute'):
        leven_distances = dict()
    
        for vocab in vocabs:
            leven_distances[vocab] =  levenshtein_distance(word, vocab)

        # sorted by distance
        sorted_distences = dict(sorted(leven_distances.items(), key = lambda item: item[1] ))
        correct_word =list(sorted_distences.keys())[0]
        st.write("Correct word: ", correct_word)

        col1, col2 = st.columns(2)
        col1.write("VOcabulary")
        col1.write(vocabs)

        col2.write("Distaces:")
        col2.write(sorted_distences)

if __name__ =="__main__":
    main()
