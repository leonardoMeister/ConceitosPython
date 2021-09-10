from datetime import date, datetime

cidade = "Monte Castelo"

data = datetime.now()
print ( str( data ) + "\n------------------------")

dia = data.day
mes = data.month
semana = date.weekday(data)
ano = data.year

data = "{}, {} do {} de {}, dia da semana {}"

print ( data.format(cidade, dia, mes, ano, semana))
