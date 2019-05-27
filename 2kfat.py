import math

def mat2():
    mat = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            line = [1, i, j]
            line.append(line[1] * line[2]) # AB
            mat.append(line)
    return mat

def mat3():
    mat = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                line = [1, i, j, k]
                line.append(line[1] * line[2])              # AB
                line.append(line[1] * line[3])              # AC
                line.append(line[2] * line[3])              # BC
                line.append(line[1] * line[2] * line[3])    # ABC
                mat.append(line)
    return mat

def mat4():
    mat = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                for l in [-1, 1]:
                    line = [1, i, j, k, l]
                    line.append(line[1] * line[2])                      # AB
                    line.append(line[1] * line[3])                      # AC
                    line.append(line[1] * line[4])                      # AD
                    line.append(line[2] * line[3])                      # BC
                    line.append(line[2] * line[4])                      # BD
                    line.append(line[3] * line[4])                      # CD
                    line.append(line[1] * line[2] * line[3])            # ABC
                    line.append(line[1] * line[2] * line[4])            # ABD
                    line.append(line[1] * line[3] * line[4])            # ACD
                    line.append(line[2] * line[3] * line[4])            # BCD
                    line.append(line[1] * line[2] * line[3] * line[4])  # ABCD
                    mat.append(line)
    return mat

def parse_input(s):
    v = s.split(',')
    for i in range(0, len(v)):
        aux = v[i].split()
        for j in range(0, len(aux)):
            aux[j] = int(aux[j])
        v[i] = aux
    return v

def media_data(data):
    med = []
    for i in range(0, len(data)):
        acum = 0
        for num in data[i]:
            acum += num
        med.append(int(acum/len(data[i])))
    return med

def sst(data, mat):
    sst = []
    q = []
    med = media_data(data)
    n = len(mat)
    k = math.log2(n)
    for i in range(0, n):
        acum = 0
        for j in range(0, n):
            acum += mat[j][i] * med[j]
        q.append(abs(acum)/n)
    for i in range(1, len(q)):
        sst.append(pow(2, k) * q[i] * q[i])
    return sst

def sse(data):
    sse = 0
    med = media_data(data)
    for i in range(0, len(data)):
        for num in data[i]:
            sse += pow(num - med[i], 2)
    return sse

def main():
    mat = []
    data = []
    k = int(input("Valor de k: "))
    if k == 2:
        mat = mat2()
    elif k == 3:
        mat = mat3()
    else:
        mat = mat4()
    data = input("Dados coletados: ")
    data = parse_input(data)
    v = sst(data, mat)
    s = sse(data)
    tot = 0
    for i in range(0, len(v)):
        tot += v[i]
    for i in range(0, len(v)):
        print("Fator {0} = {1:.2f}%".format(i+1, (v[i]/tot) * 100))
    print("Erro = {0:.2f}%".format((s/tot) * 100))

if __name__ == "__main__":
    main()
