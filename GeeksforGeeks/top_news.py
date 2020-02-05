import requests
'''
Author: Charles Garrido

Script uses an newsapi to grab the top 10 headlines from BBC
Then prints the headlines into the terminal
'''

def NewsFromBBC(): 
	main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
	open_bbc_page = requests.get(main_url).json() 
	article = open_bbc_page["articles"] 
	results = [] 
	for ar in article: 
		results.append(ar["title"]) 
	for i in range(len(results)): 
		print(i + 1, results[i])				 

if __name__ == '__main__':
        program_running = True
        while program_running is True:
                NewsFromBBC()
                kill_program = input('Press [enter] to quit.\n')
                if kill_program == '':
                        exit()
                
