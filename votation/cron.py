from votation.models import (
    Vote,
    RamenYa
)

def update_score():
    try:
        ramen_list = RamenYa.objects.all()
        for ramen in ramen_list:
            votes = Vote.objects.filter(ramen_id=ramen.id).count()
            ramen.total_votes = votes
            ramen.save()
        return 0
    except Exception as e:
        print(e)
