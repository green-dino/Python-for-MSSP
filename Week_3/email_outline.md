# Background 
[Cloudflare Explains E-mail Verification](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)

[Deployment Checklist](https://dmarcian.com/dmarc-deployment-checklist/ )

[DMARC](https://dmarc.org/)

[Training](https://www.m3aawg.org/activities/training/dmarc-training-series)

# So what's safe ? 
Spam emails are typically not safe and should be treated with caution due to the various types of attacks they may contain:

Phishing Attacks: These are common in spam emails and involve tricking recipients into revealing personal information like passwords or credit card numbers. Attackers often use spoofed emails to make them appear legitimate.

Malware Distribution: Spam emails frequently carry malware, which can be hidden within attachments, links, or images. Clicking on or downloading content from such emails can infect your device with malicious software.

Advance-Fee Scams: Another prevalent type of spam involves promises of future payments in exchange for providing money upfront. These scams prey on victims' trust and financial desperation.

Phishing emails are crafted to resemble communications from legitimate sources, making them challenging to spot. Here are key signs to look for:

Failed SPF, DKIM, or DMARC Checks: These authentication protocols verify email origins. If an email fails one or more of these checks, it's likely spam. Legitimate emails typically pass these checks and don't end up in spam folders.