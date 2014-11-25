import csv
#Open RAT Configuration file
with open('local-asa-configv1.conf', 'rb') as input_file:
	#Open new CSV file to store all config detials.
	with open('firewall.csv', 'wb') as output_file:
		writer = csv.writer(output_file)
		header=["ConfigRuleName","ConfigRuleDescription","ConfigRuleParentname","ConfigRuleChildrenNeeded","ConfigRuleQuestion","ConfigRuleOptional","ConfigRuleSelected","ConfigRuleParseOrder","ConfigRuleVersion","ConfigRuleContext","ConfigRuleInstance","ConfigRuleType","ConfigRuleMatch","ConfigRuleImportance","ConfigRuleReason","ConfigRuleDiscussion","ConfigRuleCallout","ConfigRuleFix"]
		#Write CSV header
		writer.writerow(header)
		#Declare record holder array.
		record=[]
		line_counter=0
		new_line_counter=0
		#Config Variables
		ConfigRuleName=ConfigRuleDescription=ConfigRuleParentname=ConfigRuleChildrenNeeded=ConfigRuleQuestion=ConfigRuleOptional=ConfigRuleSelected=ConfigRuleParseOrder=ConfigRuleVersion=ConfigRuleContext=ConfigRuleInstance=ConfigRuleType=ConfigRuleMatch=ConfigRuleImportance=ConfigRuleReason=ConfigRuleDiscussion=ConfigRuleCallout=ConfigRuleFix=""
		#Variables to max config parameters.
		#a=b=config_parameters=max_config_parameter=0
		rules_start_indicator=0
		for i,config_line in enumerate(input_file):
			#Below code find max Config parameter
			'''if a==1 and config_line.startswith("Config"):
				config_parameters+=1
			if a==1 and config_line.strip()=="":
				b=1
			if a==1 and b==1:
				if max_config_parameter<config_parameters:
					max_config_parameter=config_parameters
					print str(line_counter)+"   "+str(max_config_parameter)
				a=b=config_parameters=0
			if config_line.strip()=="":
				new_line_counter+=1
				a=1'''	
			#print "hi"
			if line_counter>=0:
				if config_line.strip()=="" and rules_start_indicator==1:
					record.append(ConfigRuleName.strip())
					record.append(ConfigRuleDescription.strip())
					record.append(ConfigRuleParentname.strip())
					record.append(ConfigRuleChildrenNeeded.strip())
					record.append(ConfigRuleQuestion.strip())
					record.append(ConfigRuleOptional.strip())
					record.append(ConfigRuleSelected.strip())
					record.append(ConfigRuleParseOrder.strip())
					record.append(ConfigRuleVersion.strip())
					record.append(ConfigRuleContext.strip())
					record.append(ConfigRuleInstance.strip())
					record.append(ConfigRuleType.strip())
					record.append(ConfigRuleMatch.strip())
					record.append(ConfigRuleImportance.strip())
					record.append(ConfigRuleReason.strip())
					record.append(ConfigRuleDiscussion.strip())
					record.append(ConfigRuleCallout.strip())
					record.append(ConfigRuleFix.strip())
					print record
					writer.writerow(record)
					record=[]
					ConfigRuleName=ConfigRuleDescription=ConfigRuleParentname=ConfigRuleChildrenNeeded=ConfigRuleQuestion=ConfigRuleOptional=ConfigRuleSelected=ConfigRuleParseOrder=ConfigRuleVersion=ConfigRuleContext=ConfigRuleInstance=ConfigRuleType=ConfigRuleMatch=ConfigRuleImportance=ConfigRuleReason=ConfigRuleDiscussion=ConfigRuleCallout=ConfigRuleFix=""
					rules_start_indicator=0

				if config_line.startswith("ConfigRuleName"):
					ConfigRuleName=config_line[len("ConfigRuleName:"):]
					rules_start_indicator=1			
				if config_line.startswith("ConfigRuleDescription"):
					ConfigRuleDescription=config_line[len("ConfigRuleDescription:"):]
				if config_line.startswith("ConfigRuleParentname"):
					ConfigRuleParentname=config_line[len("ConfigRuleParentname:"):]
				if config_line.startswith("ConfigRuleChildrenNeeded"):
					ConfigRuleChildrenNeeded=config_line[len("ConfigRuleChildrenNeeded:"):]
				if config_line.startswith("ConfigRuleQuestion"):
					ConfigRuleQuestion=config_line[len("ConfigRuleQuestion:"):]
				if config_line.startswith("ConfigRuleOptional"):
					ConfigRuleOptional=config_line[len("ConfigRuleOptional:"):]
				if config_line.startswith("ConfigRuleSelected"):
					ConfigRuleSelected=config_line[len("ConfigRuleSelected:"):]
				if config_line.startswith("ConfigRuleParseOrder"):
					ConfigRuleParseOrder=config_line[len("ConfigRuleParseOrder:"):]
				if config_line.startswith("ConfigRuleVersion"):
					ConfigRuleVersion=config_line[len("ConfigRuleVersion:"):]
				if config_line.startswith("ConfigRuleContext"):
					ConfigRuleContext=config_line[len("ConfigRuleContext:"):]
				if config_line.startswith("ConfigRuleInstance"):
					ConfigRuleInstance=config_line[len("ConfigRuleInstance:"):]
				if config_line.startswith("ConfigRuleType"):
					ConfigRuleType=config_line[len("ConfigRuleType:"):]
				if config_line.startswith("ConfigRuleMatch"):
					ConfigRuleMatch=config_line[len("ConfigRuleMatch:"):]
				if config_line.startswith("ConfigRuleImportance"):
					ConfigRuleImportance=config_line[len("ConfigRuleImportance:"):]
				if config_line.startswith("ConfigRuleReason"):
					ConfigRuleReason=config_line[len("ConfigRuleReason:"):]
				if config_line.startswith("ConfigRuleDiscussion"):
					ConfigRuleDiscussion=config_line[len("ConfigRuleDiscussion:"):]
				if config_line.startswith("ConfigRuleCallout"):
					ConfigRuleCallout=config_line[len("ConfigRuleCallout:"):]
				if config_line.startswith("ConfigRuleFix"):		
					ConfigRuleFix=config_line[len("ConfigRuleFix:"):]
				
			'''if line_counter==92:
				break			'''
			line_counter+=1
		
		