from .Graphics import tkinter

def FindAsk(parent,*args):
  root = tkinter.Toplevel(parent)
  root.title("Find And Replace")
  root.transient(parent)
  root.focus_force()
  root.resizable(width=0, height=0)
  root['padx']=20
  fields = {}
  field={}
 
  for r, label in enumerate(args):
    store_label = tkinter.Label(root, text=label)
    store_label.grid(row=r, column = 0, ipady=5, ipadx=20)
    store_entry = Tkinter.Entry(root)
    store_entry.grid(row=r, column=1)
    field[label]=store_entry
    fields['submit']=False

  def sub():
    for l,t in field.iteritems():
      fields[l]=t.get()
      fields['submit']=True
      root.destroy()
      return

    submit=tkinter.Button(root,text="Ok", command=sub)
    submit.grid(row=r+1, column=2)
    root.wait_window()
    return fields


class FindReplaceFunctions:
  def __init__(self,text):
    self.text = text
    self.key_binding_functions()
    self.binding_functions_configuration()

  def binding_functions_configuration(self):
    self.text.storeobj['Find'] = self.find_
    self.text.storeobj['FindAll'] = self.find_all
    self.text.storeobj['Replace'] = self.replace
    self.text.storeobj['ReplaceAll'] = self.replace_all
    return

  def key_binding_functions(self):
    for key in ['&lt;Control-F>',"&lt;Control-f>"]:
      self.text.bind(key, self.find_)
    for key in ['&lt;Control-Shift-F>',"&lt;Control-Shift-f>"]:
      self.text.bind(key, self.find_all)
    for key in ['&lt;Control-Shift-H>',"&lt;Control-Shift-h>"]:
      self.text.bind(key, self.replace_all)
    for key in ['&lt;Control-H>',"&lt;Control-h>"]:
      self.text.bind(key, self.replace)
    return


  def find_(self, event=None):
    t = FindAsk(self.text.master, "Find")
    if t['submit']:
      print (t['Find'])
    return

  def find_all(self, event=None):
    t = FindAsk(self.text.master, "FindAll")
    if t['submit']:
      print (t['FindAll'])
    return

  def replace(self, event=None):
    t = FindAsk(self.text.master, "Find", "Replace")
    if t['submit']:
      print (t['Find'])
      print (t['Replace'])
    return

  def replace_all(self, event=None):
    t = FindAsk(self.text.master, "FindAll", "ReplaceAll")
    if t['submit']:
      print (t['FindAll'])
      print (t['ReplaceAll'])
    return


if __name__ == '__main__':
  root = tkinter.Tk()
  pad = tkinter.Text(root)
  pad.pack()
  pad.storeobj={}
  FindReplaceFunctions(pad)
  # print FindAsk(root,"a","b",1)
  root.mainloop()