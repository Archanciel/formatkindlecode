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
		self.showTempConfirmAndDestroy()
		
	def showTempConfirmAndDestroy(self):
		'''
		Displays a temporary MessageBox to inform that the job was done and
		close the app.
		'''
		from tkinter import messagebox

		self._root.update() # now it stays on the clipboard after the window is closed
		self._root.after(1500, self._root.destroy) # Destroy the widget after 1.5 seconds
		try:
			if messagebox.showinfo('formatkindlecode', 'Formatted code copied to clipboard'):
				self._root.destroy()
		except:
			pass
		
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

