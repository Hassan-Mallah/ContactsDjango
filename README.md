# ContactsDjango
API to store and search contacts. Works fast with thousands of records.
--------------------------
![Alt text](https://github.com/Hassan-Mallah/ContactsDjango/blob/master/Screenshot1.png)
--------------------------
![Alt text](https://github.com/Hassan-Mallah/ContactsDjango/blob/master/Screenshot.png)

Input example JSON:
{
	"source_id": 1,
	"items": [{
		"name": "Анна",
		"phone": 9001234453,
		"email": "mail1@gmail.com"
	}, {
		"name": "Иван",
		"phone": "+79001234123",
		"email": "mail2@gmail.com"
	}]
} 
- every "source id" is a client
- phone number by the same "source id" can't be repeated in the same day.
