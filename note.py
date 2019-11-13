import os 
import sys


class NoteAuto:
    
    
    python = '.py'
    
    java = '.java'
    
    text = '.txt'
    
    dart = '.dart'
    
    yaml = '.yaml'
    
    json = '.json'
    
    html = '.html'
    
    extensions = {
        
        'pyhton':python,
        '.py':python,
        'java':java,
        '.java':java,
        'text':text,
        '.txt':text,
        'dart':dart,
        '.dart':dart,
        'flutter':dart,
        'yaml':yaml,
        '.yaml':yaml,
        'json':json,
        'jason':json,
        '.json':json,
        'html':html,
        '.html':html     
        
    }
    
    
    extension = ""
    
    fileName = ""
    
    folderName = ""
    
    path = os.getcwd()
    
    foundFileExtension = ""
    
    
    def getArgs(self,ext_num, fold_num):
        
        try:
            self.extension = str(sys.argv[ext_num]).lower()
            
            self.extension  = self.extensions[self.extension]
            
        except Exception:
            
            self.extensions = '.txt'
            
        try:
            
            self.folderName = str(sys.argv[fold_num])
            
        except Exception:
            
            self. folderName = 'Genaral'
            
        try:
             
             self.fileName = str(sys.argv[2])
             
             
        except Exception:
            
            print('Name your note')
            
            sys.exit()
    
    
    def createNoteAndFolder(self):
        
        
        os.chdir("./Notes")
        
        self.fileName = self.fileName + self.extension
        
        if os.path.isdir("./"+self.folderName):
            
            os.chdir("./"+self.folderName)
        else:
            
            os.mkdir(self.folderName)
            os.chdir("./"+self.folderName)
            
            
        if not os.path.isfile("./"+self.fileName):
            
            open(self.fileName,"a").close()
            
        os.system("code "+self.fileName)
        
        
        
if __name__ == "__main__":
    note = NoteAuto()
    
    command = str(sys.argv[1])
    
    
    if command == "nfe":
        note.getArgs(4,3)
        note.createNoteAndFolder()
        