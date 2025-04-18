import sys
def summarize_email(emailBody):
    keywords = ['help', 'deadline', 'urgent', 'sos']
    summary_lines = []

    # Split into lines or sentences
    lines = emailBody.split('\n')

    for line in lines:
        for keyword in keywords:
            if keyword.lower() in line.lower():
                summary_lines.append(line.strip())
                break  # Stop checking other keywords for this line

    if summary_lines:
        return ' | '.join(summary_lines)
    else:
        return 'No critical content detected.'
