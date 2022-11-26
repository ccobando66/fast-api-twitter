import uuid


from models.users import Users as us
from models.tweets import Tweet as tw

from datetime import datetime

from config.config import(
    conexion, Session, Base
)

from schema.tweets import Tweets

from fastapi import(
    APIRouter, status, Path,
    Body
)

tweets = APIRouter()

Base.metadata.create_all(conexion)
seccion = Session()

@tweets.get(
    path='/',
    status_code=status.HTTP_200_OK,
    tags=['Tweets']
    )
def get_all_tweets():
    get_tweets = seccion.query(tw).all()
    seccion.close()
    return get_tweets

@tweets.get(
    path='/tweets/{tweets_id}',
    status_code=status.HTTP_202_ACCEPTED,
    tags=['Tweets']
)
def get_tweets(tweets_id:str = Path(...,min_length=1)):
    get_tweet = seccion.query(tw).get(tweets_id)
    seccion.close()
    return get_tweet



@tweets.post(
    path='/tweets',
    status_code=status.HTTP_201_CREATED,
    response_model=Tweets,
    tags=['Tweets']
)
def create_tweets(tweets:Tweets = Body(...)):
    tweets.tweets_id = uuid.uuid4()
    user_tweet = seccion.query(us).get(str(tweets.by.user_id))
    tweet_recived = tw(
        id = str(tweets.tweets_id),
        content= tweets.content,
        created_at = tweets.created_at
    )
    seccion.add(tweet_recived)
    user_tweet.tweets.append(tweet_recived)
    seccion.commit()
    seccion.close()
    
    return tweets



@tweets.put(
    path='/tweets/{tweets_id}',
    status_code=status.HTTP_202_ACCEPTED,
    response_model=Tweets,
    response_model_exclude={'by'},
    tags=['Tweets']
)
def update_tweets(
    tweets_id:str = Path(...,min_length=1),
    tweets:Tweets = Body(...)
    ):
    get_tweet = seccion.query(tw).get(tweets_id)
    get_tweet.content = tweets.content
    get_tweet.update_at = datetime.now()
     
    tweets.tweets_id = get_tweet.id
    tweets.created_at = get_tweet.created_at
    tweets.update_at = get_tweet.update_at
    
    seccion.add(get_tweet) 
    seccion.commit()
    seccion.close()
    
    return tweets
    


@tweets.delete(
    path='/tweets/{tweets_id}',
    status_code=status.HTTP_202_ACCEPTED,
    tags=['Tweets']
)
def delete_tweets(tweets_id:str = Path(...,min_length=1)):
    deleted_tweets = seccion.query(tw).get(tweets_id)
    seccion.delete(deleted_tweets)
    seccion.commit()
    seccion.close()
    return deleted_tweets