from orm import Histo

class Msg:

    def __init__(self, id=0, time="", name="", msg=""):
        self.id = id
        self.time = time
        self.name = name
        self.msg = msg

    def all(self):
        dico = Histo().dico()
        lst = list()
        for el in dico:
            msg = Msg(el['id'], el['time'], el['name'], el['msg'])
            lst.append(msg)
        return lst

    def nb(self):
        return len(self.all())

    def find(self, id=0):
        msgs = self.all()
        msg = Msg()
        for m in msgs:
            if(id == m.id):
                msg = m
        return msg

    def find_int(self, id_inf=0, id_sup=1):
        if id_sup < id_inf: id_inf, id_sup = id_sup, id_inf
        msgs = self.all()
        lst = list()
        for m in msgs:
            if(m.id >= id_inf and m.id <= id_sup):
                lst.append(m)
        return lst

    def by_name(self, name=""):
        msgs = self.all()
        lst = list()
        for m in msgs:
            if name in m.name:
                lst.append(m)
        return lst
    def nb_by_name(self, name=""):
        return len(self.by_name(name))

    def get_all_names(self):
        msgs = self.all()
        lst = list()
        for m in msgs:
            if len(lst) == 0: lst.append(m.name)
            if m.name not in lst:
                lst.append(m.name)
        return lst

    def msgs_by_names(self):
        msgs = self.all()
        lst = list()
        dico = {'name': "", 'msgs': []}
        dico['name'] = msgs[0].name
        dico['msgs'].append(msgs[0])
        lst.append(dico)
        for m in msgs:
            for i,d in enumerate(lst):
                if(m.name in d['name']):
                    lst[i]['msgs'].append(m)
                else:
                    dico = {'name': "", 'msgs': []}
                    dico['name'] = m.name
                    dico['msgs'].append(m)
                    lst.append(dico)
        return lst