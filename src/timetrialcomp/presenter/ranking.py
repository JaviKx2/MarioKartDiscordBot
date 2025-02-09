from src.shared.domain.errors import has_errors, DomainError
from src.timetrialcomp.competition.infrastructure.dependency_injection import time_submitter
from src.timetrialcomp.shared.presenter import render_error_message


async def present_ranking(ttcomp_id, find_user) -> str:
    ranking_response = time_submitter.ranking(ttcomp_id)

    if has_errors(ranking_response):
        return render_error_message(ranking_response)

    if len(ranking_response) == 0:
        return f"```No times submitted yet.```"

    max_len = 0
    display_names = dict()
    for row in ranking_response:
        user = await find_user(row['player_id'])
        display_names.update({row['player_id']: user.display_name})
        max_len = max(max_len, len(user.display_name))

    view_rows = "🏆 Ranking\n"
    for i, row in enumerate(ranking_response):
        view_rows += (
            f"{render_position(i)} "
            f"{display_names[row['player_id']].ljust(max_len)} "
            f"🕒 {row['time']} "
            f"{'✔' if row['approved'] else '❌'}"
            f"\n"
        )

    return f"```{view_rows}```"


def render_position(index):
    positions = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    if 0 <= index < len(positions):
        return positions[index]

    return str(index + 1)