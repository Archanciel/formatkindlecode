try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk

import re

class KindleCodeFormater():

	def __init__(self):
		self._root = Tk()
		self._roughKindleCode = self._root.clipboard_get()
		self._formatedKindleCode = ''
		
	def formatCode(self):
		codeWithNoSpaceInMatrix = self._removeSpaceInMatrices(self._roughKindleCode)
		fixedPlottingComment = self._fixPlottingComment(codeWithNoSpaceInMatrix) 
		codeWithLineBreak = re.sub(r"; ", r";\n", fixedPlottingComment)
		self._formatedKindleCode = codeWithLineBreak

	def formatedCodeToClipboard(self):
		self._root.clipboard_append(self._formatedKindleCode)
		self._root.update() # now it stays on the clipboard after the window is closed
		self._root.destroy() 
		
	def _removeSpaceInMatrices(self, codeStr):
		pattern = r"(\[[\d\w ;]+\])"
		noSpaceMatrix = ''
		
		for match in re.finditer(pattern, codeStr):
			roughMatrix = match.group()
			
			if '; ' in roughMatrix:
				noSpaceMatrix = roughMatrix.replace('; ', ';')
				codeStr = codeStr.replace(roughMatrix, noSpaceMatrix)
				
		return codeStr
		
	def _fixPlottingComment(self, codeStr):
		codeStr = codeStr.replace("%plotting ", "\n\n%plotting\n")
				
		return codeStr
    	
if __name__ == '__main__':
	formater = KindleCodeFormater()
	formater.formatCode()
	formater.formatedCodeToClipboard()

