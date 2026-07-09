import pandas as pd
import seaborn as sb
from matplotlib.pyplot import show
df=pd.read_csv('Spotify_Youtube Dataset.csv')
df.drop(['Unnamed: 0'],inplace=True,axis=1)
df.fillna({'Likes':0,'Comments':0},inplace=True)
df.dropna(inplace=True)
top_10_youtube_artists=df.groupby('Artist')['Views'].sum().sort_values(ascending=False)
top_10_tracks=df.groupby('Track')['Stream'].sum().sort_values(ascending=False)
most_common_album=df['Album_type'].value_counts().reset_index()
average_album_types=df.groupby('Album_type')[['Views','Likes','Comments']].mean(numeric_only=True).reset_index()
average_album_types=pd.melt(average_album_types,id_vars='Album_type',var_name='Attribute',value_name='Total')
top_5_youtube_channels_based_on_views=df.groupby(by='Channel').sum(numeric_only=True).sort_values(by='Views',ascending=False)['Views'].head(5)
top_viewed_track=df.groupby('Track').sum(numeric_only=True).sort_values('Views',ascending=False)['Views'].head(1)
top_viewed_track2=df['Track'].max(numeric_only=True)
df['like/view']=round(df['Likes']*100/df['Views'],0)
top_7_tracks_like_view_ratio=df.sort_values(by='like/view',ascending=False)[['Track','like/view']].head(7)
top_Danceability_album=df.groupby('Album')['Danceability'].sum().sort_values(ascending=False)
coorelation_likes_comments_views=df[['Likes','Comments','Views','Stream']]
sb.heatmap(coorelation_likes_comments_views.corr())
show()