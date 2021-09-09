CREATE TABLE "learning" (
    "tweet" varchar,
    "positivity_rank" int
);

DROP  Table tweet_data;

CREATE TABLE tweet_data (
	"id" serial,
	"name" varchar,
	"date" varchar,
	"retweet_count" int,
    "tweet_text" varchar,
    "tweet_cleaned" varchar,
    "search_key" varchar,
    "est_positivity" int,
	primary key(id)
);