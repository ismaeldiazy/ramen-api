from votation.models import (
    RamenScore,
    Vote
)

def update_score():
    try:
        ramen_list = RamenScore.objects.all()
        for ramen in ramen_list:
            votes = Vote.objects.filter(ramen_id=ramen.id).count()
            ramen.total_votes = votes
            ramen.save()
        print('Ramen Scores updated!!')
        return 0
    except Exception as e:
        print(e)
