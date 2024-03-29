import time, sys
from PyQt4 import QtGui,QtCore
from Test_interface import Ui_MainWindow

import pymedia.audio.sound as sound
import pymedia.audio.acodec as acodec

class Test_one(QtGui.QMainWindow):
	def __init__(self,Parent = None):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#self.initUI()
		
		# connect in button line
		
	#def initUI(self):
		
		self.ui.connect(self.ui.pushButton, QtCore.SIGNAL('buttonPressed(int)'), self.VoiceRecord)
		
		#self.ui.button_open.clicked.connect(self.voiceRecorder)
		
		
	def voiceRecorder(self, initUI,secs, channels, name ):
		f= open( name, 'wb' )
	  # Minimum set of parameters we need to create Encoder
		cparams= { 'id': acodec.getCodecID( 'mp3' ),
				 'bitrate': 138000,
				 'sample_rate': 44100,
				 'channels': channels } 
		ac= acodec.Encoder( cparams )
		snd= sound.Input( 44100, channels, sound.AFMT_S16_LE )
		snd.start()
	  
	  # Loop until recorded position greater than the limit specified
		while snd.getPosition()<= secs:
			s= snd.getData()
		if s and len( s ):
		  for fr in ac.encode( s ):
			# We definitely should use mux first, but for
			# simplicity reasons this way it'll work also
			f.write( fr )
		else:
		  time.sleep( .003 )
	  
	  # Stop listening the incoming sound from the microphone or line in
		snd.stop()

	# ----------------------------------------------------------------------------------
	# Record stereo sound from the line in or microphone and save it as mp3 file
	# Specify length and output file name
	# http://pymedia.org/
#if __name__ == "__main__":
if len( sys.argv )!= 4:
	print 'Usage: voice_recorder <seconds> <channels> <file_name>'
else:
	voiceRecorder( int( sys.argv[ 1 ] ), int( sys.argv[ 2 ] ), sys.argv[ 3 ]  )

				
				
				
			  

				
			
			
			

if __name__ == "__main__":
	#app = QtGui.QApplication(sys,argv)
	myapp =  Test_one()
	myapp.show()
	sys.exit(app.exec__())
			
