import matplotlib.pyplot as plt

def frequencyPerLength(genome, length, nucleotide):
    start = 0
    end = start+length
    frequency = []
    count = 0
    while end < len(genome):
        for i in range(start, end):
            if genome[i] == nucleotide:
                count += 1
        start = end
        end = end+length
        frequency.append(count)
        count = 0
    return frequency

def getFrequency(genome, nucleotide):
    count = 0
    for n in genome:
        if n == nucleotide:
            count += 1
    return count

def main():
    file = open('covid_genome.txt')
    genome = file.read().replace('\n', '')
    file.close()
    labels = 'A', 'T', 'C', 'G'


    #frequency = [getFrequency(genome, 'A'),getFrequency(genome, 'T'),getFrequency(genome, 'C'),getFrequency(genome, 'G')]
    #fig, ax1 = plt.subplots()
    #ax1.pie(frequency, labels = labels)
    #ax1.axis('equal')
    #plt.show()

    x = frequencyPerLength(genome, 100, 'A')
    plt.hist(x, bins = 100)
    plt.xlabel('Number of Adenines per 100 Bases in Sequence')
    plt.ylabel('Frequency')
    plt.show()

main()