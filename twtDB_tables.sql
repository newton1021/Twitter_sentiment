
DROP  Table tweet_data;

CREATE TABLE tweet_data (
	"id" serial primary key,
	"name" varchar,
	"date" varchar,
	"retweet_count" int,
    "tweet_text" varchar,
    "tweet_cleaned" varchar,
    "search_key" varchar,
    "est_positivity" int
);


