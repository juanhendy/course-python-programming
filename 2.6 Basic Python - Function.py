def halo_dunia():
    var = 'Halo Python, halo dunia'
    print(var)
halo_dunia()

def selamat_datang(nama):
    var = f'Halo {nama}, welcome'
    print(var)
selamat_datang('Asep')
selamat_datang('Juna')

x = 100
def operasi(a, b, c=2):
    op1 = a + b
    op2 = op1 / c
    print('a di dalam function:', a)
    print('b, di dalam function', b)
    print(x)
    return op2
hasil = operasi(a=10, b=5)
print(hasil)