from models import Msg
def waiting():
    input()

if __name__ == '__main__':
    msgs = Msg()
    """
    print("Nombre Total : ", msgs.nb())
    print("[Kajun] Nombre msgs : ", msgs.nb_by_name('Kajun'))
    print("[JC] Nombre msgs : ", msgs.nb_by_name('JC'))
    d = msgs.find(10)
    print('\tMsg: 10 is: \n', 'id: {0}\ttime: {1}\tname: {2}\tmsg: {3}'.format(d.id, d.time, d.name, d.msg),'\n')

    print('\tAll Messages from [Kajun] : ')
    for d in msgs.by_name('Kajun'):
        print('id: {0}\ttime: {1}\tname: {2}\tmsg: {3}'.format(d.id,d.time,d.name,d.msg))

    print('\tAll Messages from [JC] : ')
    for d in msgs.by_name('JC'):
        print('id: {0}\ttime: {1}\tname: {2}\tmsg: {3}'.format(d.id, d.time, d.name, d.msg))
    
    """

    #print('\tAfficher tout les noms {}: '.format(len(msgs.get_all_names())))
    #for name in msgs.get_all_names():
        #print(' - ', name, '-')

    for d in msgs.all():
        print('id: {0}\ttime: {1}\tname: {2}\tmsg: {3}'.format(d.id,d.time,d.name,d.msg))
        waiting()