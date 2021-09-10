import pandas

dicionarioAlunos = {'Nome':["leonardo","verônica","Clemir"],
                    'Nota':[10,9.5,7],
                    'idade':[20,41,43]}

alunosDF = pandas.DataFrame(dicionarioAlunos)

print(alunosDF)
