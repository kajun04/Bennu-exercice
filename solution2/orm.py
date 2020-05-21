import re

dico = {
    'id':1,
    'time': "5/13/20, 10:24 AM",
    'name': "Kajun'ss",
    'msg': "Je te comprends tout a fait bro.."
}

class Histo:

    def __init__(self, file = str('')):
        if(len(file) == 0):
            self.file_name = 'data/data.txt'
        else: self.file_name = file

    def string(self):
        try:
            with open(self.file_name, 'r') as file:
                data = file.read()
        except:
            return ""
        return data

    def list(self):
        return self.string().split('\n')

    def messages(self):
        msgs = list()
        ch_exp = r"^(([0-9]{1,2}/?){3}, ([0-9]{1,2}:?){2} (AM|PM) -)"
        exp = re.compile(ch_exp)
        for l in self.list():
            if exp.match(l) is not None:
                msgs.append(l)
            else:
                last = len(msgs)
                if last != 0:
                    element = msgs[last-1]
                    element = element+'\n'+l
                    msgs[last-1] = element
        return msgs

    def dico(self):
        dico_list = list()
        ch_exp = r"(?P<time>(([0-9]{1,2}/?){3}, ([0-9]{1,2}:?){2} (AM|PM))) - (.*): ((.*\n*)*)"
        exp = re.compile(ch_exp)
        for i,m in enumerate(self.messages()):
            msg_list = exp.match(m)
            if (msg_list is not None):
                d = {'id': 0,'time': "",'name': "",'msg': ""}
                d['id'] = i
                d['time'] = msg_list.groups()[0]
                d['name'] = msg_list.groups()[5].split(':')[0]
                d['msg'] = msg_list.groups()[6]
                dico_list.append(d)
        return dico_list