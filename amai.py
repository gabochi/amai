class automap:
    def __init__(self, all_data):
        self.fields = set()
        self.tuplas = []
        
        def r(data, path):
            if type(data) in {dict,list}:
                if isinstance(data,dict):
                    for k,v in data.items():
                        self.fields.add("_".join(path+[k]))
                        r(v,path+[k])
                else:
                    for i in data:
                        r(i,path)
            else:
                self.tuplas.append(("_".join(path),data))
        
        r(all_data,[])
        
"""
# Auto Map And Insert

from datetime import datetime

class amai:
    
    def __init__(self, inputd, root):
        self.fields = set() 
        self.rows = []
        self.outputd = []
        self.outputd.append({})

        def recursive_iteration(l, d, path):
            
            for k, v in d.items():
                if isinstance(v, list):
                    for n, i in enumerate(v):
                        recursive_iteration(n, i, f'{path}_{k}')
                else:
                    if isinstance(v, dict):
                        recursive_iteration(l, v, f'{path}_{k}')
                    else:
                        try:
                            x = self.outputd[l]
                        except IndexError:
                            self.outputd.append({})

                        if f'{path}_{k}' in self.fields:
                            #print(f"duplicate : {path}_{k}")
                            pass
                        else:
                            #print(f"NEW : {path}_{k}")
                            self.fields.add(f'{path}_{k}')
                        
                        self.outputd[l][f'{path}_{k}'] = str(v)
            
        recursive_iteration(0, inputd, root)
        self.fields = sorted(self.fields) 
        
        for r in range(len(self.outputd)):
            self.rows.append([])
            for n, f in enumerate(self.fields):
                self.rows[r].append(self.outputd[0][f])
                try:
                    self.rows[r][n] = self.outputd[r][f]
                except:
                    pass


    def insert(self, table, connect):
        
        cursor = connect.cursor()

        self.fields.append('fecha_creacion')
        fecha_creacion = datetime.now()

        for r in range(len(self.rows)):
            self.rows[r].append(fecha_creacion)

        fields = ",".join(self.fields)
        number = []

        # check table cols
        tablefields = set()
        cursor.execute(f'select * from {table}')
        cursor.fetchone()
        for f in cursor.description:
            tablefields.add(f[0])

        for n, f in enumerate(self.fields):
            number.append(f':{n+1}')
            
            thisfield = str(f).upper()
            if thisfield not in tablefields:
                print(f'adding {thisfield}')
                cursor.execute(f'alter table {table} add {thisfield} varchar2(256)')
        
        binds = ",".join(number)
        command = f'insert into {table} ({fields}) values ({binds})'
        
        print(command, self.rows)
        cursor.executemany(command, self.rows)
        connect.commit()
"""
