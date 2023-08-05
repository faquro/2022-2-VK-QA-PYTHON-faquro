#!bin/bash
file=$1
exit_file=$2
if [ -z "$2" ]
then
        exit_file=result.txt
fi
if [ -n "$1" ]
then
	echo "Info from file: $file" > $exit_file
	echo -e "\nTotal count:" >> $exit_file
	cat $file | awk '{print $1}' | wc -l >> $exit_file
	echo -e "\nTotal by type:" >> $exit_file
	for var in "GET" "POST" "HEAD" "PUT"
    do
        (echo -n "$var " ; cat $file | awk 'length($6)<10{print substr($6,2)}' | grep -w "$var" | wc -l) >> $exit_file
    done
	echo -e "\nTop 10 most frequent requests:" >> $exit_file
    cat $file | awk '{print $7}' | sort | uniq -c | sort -rn | head -n 10 >> $exit_file
	echo -e "\nTop 5 biggest queries with error 4XX:" >> $exit_file
    cat $file | awk 'int($9/100)==4 {print $1,$9,$7,$10}' |  sort -rnk4 | head -n 5 >> $exit_file
	echo -e "\nTop 5 users by number of requests with error 5XX:" >> $exit_file
    cat $file | awk 'int($9/100)==5 {print $1}' | sort | uniq -c | sort -rn | head -n 5 >> $exit_file
fi
