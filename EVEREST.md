# Everest fork — operating rules (read before any edit or draft)

Fork of [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) (MIT, © Sergey Bulaev — LICENSE kept unchanged), cut down for founder content on LinkedIn for Everest Capital USA / BidDeed.AI.

## What was kept (7 skills, all draft-only)
post-writer · hook-extractor · humanizer (incl. `--mode audit`) · profile-optimizer · content-planner · repurposer · interviewer

## What was removed and why
| Removed | Why |
|---|---|
| comment-drafter, reply-handler, thread-monitor, engager-analytics | Built on Apify actors that scrape LinkedIn posts, commenters and likers. LinkedIn's User Agreement prohibits scraping; the account at risk is the founder's personal brand. |
| employee-advocacy | Solo founder — no team to run it. |

## Hard rules
1. **No auto-publish.** Never set `PUBLORA_API_KEY`, `APIFY_TOKEN` or `PIXFARO_API_KEY`. With none set, `lib.publish` routes to manual copy-paste. Publora is a new third-party integration and needs the founder's explicit approval first.
2. **Human approval before anything goes out.** The founder posts by hand.
3. **Links go in the first comment**, never the post body. Every link carries `?utm_source=linkedin&utm_medium=organic&utm_campaign=founder`.
4. **Every figure needs a citable source** (clerk record, recorded instrument, county roll, or the founder's own site). No source → the number does not ship. Only figures in `references/story-bank.md` may be used; never invent one.
5. **This repo is PUBLIC** (forks of public repos cannot be private). The Story Bank and Voice Profile hold only facts already published on everestcapitalusa.com / biddeed.ai. Nothing private, no family, no financing, no internal tooling.
6. **Revenue test:** a post is "done" only if it points at a revenue surface (biddeed.ai `/buy-report` or a tier on `/subscribe`). Brand-only posts are fine but are not counted as delivery.

## Syncing upstream
`git fetch upstream && git merge upstream/main`, then re-delete the five removed skill folders and re-run `python3 -m unittest discover -s tests`. `tests/test_everest_policy.py` fails if a removed skill or a publishing key comes back.
