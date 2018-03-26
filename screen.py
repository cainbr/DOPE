from __future__ import division
import os, sys, datetime

import 	calc.calculations		as		calc

from	kivy.config 			import	Config
from 	kivy.app				import	App
from 	kivy.lang				import	Builder
from	kivy.uix.screenmanager	import	ScreenManager, Screen
from	kivy.uix.togglebutton	import	ToggleButton
from	kivy.uix.checkbox		import 	CheckBox
from	kivy.uix.widget			import	Widget
from	kivy.uix.popup			import 	Popup
from	kivy.uix.label			import	Label

from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior



from	kivy.uix.slider			import	Slider
from	kivy.graphics			import 	Color, Ellipse
from	kivy.properties			import	ObjectProperty, StringProperty, BooleanProperty

Config.set('graphics', 'fullscreen', 'auto')

os.system('clear')


cwd		=	os.getcwd()

#The following 3 lines find all KV files within the working directory.  After they are
#found, the Builder method loads them.  Each of the KV files used in this application
#are built into their individual screens.

for x in os.listdir(cwd):
	if x.lower().endswith('.kv'):
		Builder.load_file(x)



#=========================================================================================
#
#	Name:	Get DOPE Data
#	
#	This function gets all data from the DOPE screen and returns it in a dictionary 
#	format.
#
#		Inputs:	None
#
#		Output:	Location Data (Dictionary)
#				Rifle Data (Dictionary)
#				Cartridge Data (Dictionary)
#
#=========================================================================================		
def get_dope_data():
	location_data	=	{
							'Date'				:	sm.get_screen('dope').ids.date.text,
							'Location'			:	sm.get_screen('dope').ids.location.text,
							'Altitude'			:	sm.get_screen('dope').ids.altitude.text,
							'Temp'				:	sm.get_screen('dope').ids.temp.text,
							'Pressure'			:	sm.get_screen('dope').ids.baro.text,
							'Humidity'			:	sm.get_screen('dope').ids.humidity.text
						}
						
	rifle_data		=	{
							'Rifle Make'		:	sm.get_screen('dope').ids.rifle_make.text,
							'Rifle Model'		:	sm.get_screen('dope').ids.rifle_model.text,
							'Optic Make'		:	sm.get_screen('dope').ids.optic_make.text,
							'Optic Model'		:	sm.get_screen('dope').ids.optic_model.text
						}
						
	cartridge_data	=	{
							'Bullet Make'		:	sm.get_screen('dope').ids.bullet_make.text,
							'Bullet Model'		:	sm.get_screen('dope').ids.bullet_model.text,
							'Bullet Diameter'	:	sm.get_screen('dope').ids.bullet_diameter.text,
							'Bullet Weight'		:	sm.get_screen('dope').ids.bullet_weight.text,
							'Powder Make'		:	sm.get_screen('dope').ids.powder_make.text,
							'Powder Model'		:	sm.get_screen('dope').ids.powder_model.text,
							'Powder Weight'		:	sm.get_screen('dope').ids.powder_weight.text,
							'Primer Make'		:	sm.get_screen('dope').ids.primer_make.text,
							'Primer Model'		:	sm.get_screen('dope').ids.primer_model.text,
							'Primer Size'		:	sm.get_screen('dope').ids.primer_size.text
						}
				
	return (location_data, rifle_data, cartridge_data)
	
#=========================================================================================
#
#	Name:	Get Shot Data
#	
#	This function gets shot information from the Shot Data screen and returns the
#	information in a dictionary format.  The output data contains: velocity information,
#	elevation hold, wind hold, and the shooter's call.
#
#		Inputs:	None
#
#		Output:	Shot Data (Dictionary)
#
#=========================================================================================
	
def get_shot_data():
	data	=	{
					'1'				:	{
											'Velocity'	:	sm.get_screen('shot_data').ids.velocity_1.text,
											'Elev Hold'	:	sm.get_screen('shot_data').ids.elev_hold_1.text,
											'Wind Hold'	:	sm.get_screen('shot_data').ids.wind_hold_1.text
											#'Call'		:	sm.get_screen('shot_data').ids.call_1.active
										},
							
					'2'				:	{
											'Velocity'	:	sm.get_screen('shot_data').ids.velocity_2.text,
											'Elev Hold'	:	sm.get_screen('shot_data').ids.elev_hold_2.text,
											'Wind Hold'	:	sm.get_screen('shot_data').ids.wind_hold_2.text
											#'Call'		:	sm.get_screen('shot_data').ids.call_1.active
										},
							
					'3'				:	{
											'Velocity'	:	sm.get_screen('shot_data').ids.velocity_3.text,
											'Elev Hold'	:	sm.get_screen('shot_data').ids.elev_hold_3.text,
											'Wind Hold'	:	sm.get_screen('shot_data').ids.wind_hold_3.text
											#'Call'		:	sm.get_screen('shot_data').ids.call_3.active
										},
				}
				
	return data
	
class Rifle(Screen, Popup):
	pass
	
# Declare DOPE Book screen
class DOPE(Screen):
	time				=	str(datetime.datetime.now().strftime('%H:%M'))
	date				=	str(datetime.datetime.now().strftime('%d-%b-%y'))
	
	 
	
#Declare Shot Data screen
class Shot_Data(Screen):
	calc_avg_vel		=	StringProperty("0")
	calc_std_dev		=	StringProperty('0')
	calc_es				=	StringProperty('0')
	init_data_value		=	StringProperty('0.0')

	def calc_shot_data(self):
		add				=	0
		velocity_list	=	[]
		shot_data		=	get_shot_data()
		for shot, entry in shot_data.iteritems():
			for data, value in entry.iteritems():
				if data.lower() == 'velocity':
					velocity_list.append(float(value))
					
		avg_velocity	=	calc.mean_average(velocity_list)
		std_dev			=	calc.standard_dev(velocity_list)
		es				=	calc.extreme_spread(velocity_list)
					
		
			
		self.calc_avg_vel	=	str(avg_velocity)
		self.calc_std_dev	=	str(std_dev)
		self.calc_es		=	str(es)
			
		
    
#Declare Ballistics Calculator screen
class Ballistics_Calc(Screen):
    def print_to_console(self):
		print 'Something to console'
    
#Declare Target Card
class Target_Card(Screen):
	pass
	
	
#=========================================================================================
#
#	WARNING!!! EXPERIMENTAL CODE AHEAD
#
#=========================================================================================

class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(15)]
        
#=========================================================================================
#
#	END EXPERIMENTAL CODE
#
#=========================================================================================

    


# Create the screen manager
sm = ScreenManager()
sm.add_widget(DOPE(name='dope'))
sm.add_widget(Ballistics_Calc(name='bcalc'))
sm.add_widget(Shot_Data(name='shot_data'))
sm.add_widget(Target_Card(name='target_card'))

# Create the main app
class TestApp(App):
	
	def build(self):
		return sm
        
	def exit(self):
		#screen_data						=	get_screen_data()							# The plan is to get this function smaller.  Hopefully this can be
		date							=	sm.get_screen('dope').ids.date.text				# accomplished by creating the 'get_screen_data' function and use 
		time							=	sm.get_screen('dope').ids.time.text				# it to pass all the information down where it can be written to a
		distance						=	sm.get_screen('dope').ids.distance.text			# JSON file.
		
		
		location, rifle, cartridge		=	get_dope_data()
		shot_data						=	get_shot_data()
		
		dope_screen						=	[location, rifle, cartridge]
							
		print 'Distance to Target: {0}'.format(distance)
		print 'Date: {0}'.format(date)
		print 'Time: {0}'.format(time)
		print ''
										
		for x in dope_screen:
			for data_point, data in sorted(x.iteritems()):
				print '{0}: {1}'.format(data_point, data)
			print ''
			
		for key, value in sorted(shot_data.iteritems()):
			print 'Shot {0}:'.format(key)
			for shot, data in sorted(value.iteritems()):
				print '{0}: {1}'.format(shot, data)
			print ''
			
		sys.exit()
	
	
		
		

if __name__ == '__main__':
    TestApp().run()
