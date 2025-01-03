## goto_human

**Author:** evanchen
**Version:** 0.0.1
**Date:** 2025-01-02 21:34:38.230712 &#43;0800 CST m=&#43;58.651056043
**Type:** tool

### Description

[User Guide](https://local-carp-52a.notion.site/gotohuman-1704490152f08087be79c90f1fdde2ed?pvs=4)

A community implementation of human-in-the-loop functionality using [GoToHuman](https://www.gotohuman.com/), enabling asynchronous review capabilities. When AI workflows contain unstable outputs, the GoToHuman tool can create rich review interfaces for any output variables from Dify workflow nodes.


![GoToHuman Flow](./goto_human/_assets/image.png)

Key features:
- Create customizable review pages with various frontend components
- Comprehensive review management backend
- Automatic review task creation when workflow reaches designated nodes
- Asynchronous human review process with edit, approve, and reject actions
- Webhook callbacks to endpoints when review status changes
- Ability to trigger reverse calls to other Dify apps from the endpoint


Flow:
1. Workflow reaches a GoToHuman node
2. Variables are sent to GoToHuman to create a review task
3. Human reviewers can asynchronously:
   - View the data in a customized interface
   - Edit values if needed
   - Approve or reject the review
4. On status update, GoToHuman sends a webhook to the endpoint
5. Endpoint processes the review result and can trigger another Dify app workflow

![GoToHuman Flow](./goto_human/_assets/image%20copy.png)





This enables quality control and human oversight at any point in your AI workflows while maintaining asynchronous operation.


