-- Table: public.tweet_data

-- DROP TABLE public.tweet_data;

CREATE TABLE public.tweet_data
(
    id bigint,
    name text COLLATE pg_catalog."default",
    date text COLLATE pg_catalog."default",
    retweet_count bigint,
    tweet_text text COLLATE pg_catalog."default",
    tweet_cleaned text COLLATE pg_catalog."default",
    search_key text COLLATE pg_catalog."default",
    est_positivity bigint
)

TABLESPACE pg_default;

ALTER TABLE public.tweet_data
    OWNER to postgres;
-- Index: ix_tweet_data_id

-- DROP INDEX public.ix_tweet_data_id;

CREATE INDEX ix_tweet_data_id
    ON public.tweet_data USING btree
    (id ASC NULLS LAST)
    TABLESPACE pg_default;