<?php			
		$file = fopen("wi-gsmc-mys-sw010-confg.cfg","r");
		$config_counter=1;
		$counter=0;
		$not_found=0;
		while(! feof($file))
		{
			$input_command=fgets($file);
			//$file_handle = fopen("regex.csv", "r");
			$file_handle = fopen("switch.csv", "r");
			//$fields=array("regex");
			//fputcsv($file_handle1, $fields);
			$found=0;
			$rules_counter=1;
			while (!feof($file_handle)) 
			{
				$line_of_text = fgetcsv($file_handle);
				//print "\nInput: ".trim($input_command)."\t Regex: ".trim($line_of_text[0]);
				if(preg_match("/".trim($line_of_text[12])."/",trim($input_command))==1)
				{
					print "Input: ".trim($input_command)."\t Regex: ".trim($line_of_text[12])."\tGot at:".$rules_counter." and config: ".$config_counter."\n";
					$counter++;
					$found=1;
					break;
				}
				$rules_counter++;
				//fputcsv($file_handle, array(trim($line_of_text[0])));
			}
			if($found==0)
				$not_found++;

			//fclose($file_handle1);
			fclose($file_handle);
			$config_counter++;
			
		}echo "$counter\n";
		echo $not_found;
		fclose($file);
?>