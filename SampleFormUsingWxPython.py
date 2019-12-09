import wx

ADD_BUTTON_ID = 1
SUBTRACT_BUTTON_ID = 2
class Form(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Form - Calculate', size=(600,400))
        self.Pan = wx.Panel(self, -1)

        self.stNum1 = wx.StaticText(self.Pan, label='Number 1', pos=(10, 40), size=(70, 20))
        self.tcNumber1 = wx.TextCtrl(self.Pan, pos=(80, 40), size=(70, 20), style=wx.TE_RIGHT)

        self.stNum2 = wx.StaticText(self.Pan, label='Number 2', pos=(10, 70), size=(70, 20))
        self.tcNumber2 = wx.TextCtrl(self.Pan, pos=(80, 70), size=(70, 20), style=wx.TE_RIGHT)

        self.stResult = wx.StaticText(self.Pan, label='Result', pos=(10, 100), size=(70, 20))
        self.tcResult = wx.TextCtrl(self.Pan, pos=(80, 100), size=(70, 20), style=wx.TE_RIGHT)

        self.btnAdd = wx.Button(self.Pan, id=ADD_BUTTON_ID, label='Add', pos=(10, 130), size=(50,20))
        self.btnAdd.Bind(wx.EVT_BUTTON, self.Evt_Calculate) #subscribe to the event

        self.btnSubtract = wx.Button(self.Pan, id=SUBTRACT_BUTTON_ID, label='Subtract', pos=(100, 130), size=(50,20))
        self.btnSubtract.Bind(wx.EVT_BUTTON, self.Evt_Calculate) #subscribe to the event
        self.Pan.Bind(wx.EVT_SIZE, self.Evt_Resize)

    def Evt_Calculate(self, evt):
        nButtonId = evt.GetId()

        if nButtonId == ADD_BUTTON_ID:
            self.Addition()
        elif nButtonId == SUBTRACT_BUTTON_ID:
            self.Subtraction()

    def Addition(self):
        try:
            num1 = int(self.tcNumber1.Value)
            num2 = int(self.tcNumber2.Value)

            self.tcResult.Value = str(num1 + num2)
        except Exception as err:
            wx.MessageBox(str(err))

    def Subtraction(self):
        try:
            num1 = int(self.tcNumber1.Value)
            num2 = int(self.tcNumber2.Value)

            self.tcResult.Value = str(num1 - num2)
        except Exception as err:
            wx.MessageBox(str(err))

    def Evt_Resize(self, evt):
        nHeight = self.GetSize()[1]
        nWidth = self.GetSize()[0]
        
        self.btnAdd.SetPosition((10, (nHeight -60)))
        self.btnSubtract.SetPosition(((nWidth-70), (nHeight -60)))
if __name__ == '__main__':
    app = wx.App()
    Form().Show()
    app.MainLoop()        