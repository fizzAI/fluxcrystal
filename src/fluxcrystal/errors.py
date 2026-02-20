from __future__ import annotations

from typing import Any


# ---------------------------------------------------------------------------
# Base
# ---------------------------------------------------------------------------

class FluxCrystalError(Exception):
    """Base exception for all FluxCrystal errors."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


# ---------------------------------------------------------------------------
# Authentication & Authorization
# ---------------------------------------------------------------------------

class AccessDeniedError(FluxCrystalError):
    """Access denied to the requested resource."""


class AccountDisabledError(FluxCrystalError):
    """Account has been disabled."""


class BadGatewayError(FluxCrystalError):
    """Bad gateway error from the server."""


class BadRequestError(FluxCrystalError):
    """Bad request – invalid parameters."""


class BlueskyOAuthAuthorizationFailedError(FluxCrystalError):
    """Bluesky OAuth authorization failed."""


class BlueskyOAuthCallbackFailedError(FluxCrystalError):
    """Bluesky OAuth callback failed."""


class BlueskyOAuthNotEnabledError(FluxCrystalError):
    """Bluesky OAuth is not enabled."""


class BlueskyOAuthSessionExpiredError(FluxCrystalError):
    """Bluesky OAuth session has expired."""


class BlueskyOAuthStateInvalidError(FluxCrystalError):
    """Bluesky OAuth state is invalid."""


# ---------------------------------------------------------------------------
# Account Status
# ---------------------------------------------------------------------------

class AccountScheduledForDeletionError(FluxCrystalError):
    """Account is scheduled for deletion."""


class AccountSuspendedPermanentlyError(FluxCrystalError):
    """Account has been permanently suspended."""


class AccountSuspendedTemporarilyError(FluxCrystalError):
    """Account has been temporarily suspended."""


class AccountSuspiciousActivityError(FluxCrystalError):
    """Suspicious activity detected on account."""


class AccountTooNewForGuildError(FluxCrystalError):
    """Account is too new to join this guild."""


# ---------------------------------------------------------------------------
# ACL & Permissions
# ---------------------------------------------------------------------------

class ACLsMustBeNonEmptyError(FluxCrystalError):
    """ACLs must be non-empty."""


class MissingACLError(FluxCrystalError):
    """Missing ACL for the requested operation."""


class InvalidACLsFormatError(FluxCrystalError):
    """Invalid format for ACLs."""


# ---------------------------------------------------------------------------
# API Keys
# ---------------------------------------------------------------------------

class AdminAPIKeyNotFoundError(FluxCrystalError):
    """Admin API key not found."""


class NotOwnerOfAdminAPIKeyError(FluxCrystalError):
    """User is not the owner of the admin API key."""


# ---------------------------------------------------------------------------
# Applications
# ---------------------------------------------------------------------------

class ApplicationNotFoundError(FluxCrystalError):
    """Application not found."""


class ApplicationNotOwnedError(FluxCrystalError):
    """Application is not owned by the user."""


class BotApplicationNotFoundError(FluxCrystalError):
    """Bot application not found."""


class NotABotApplicationError(FluxCrystalError):
    """The application is not a bot application."""


# ---------------------------------------------------------------------------
# Bot-Specific
# ---------------------------------------------------------------------------

class BotAlreadyInGuildError(FluxCrystalError):
    """Bot is already in the guild."""


class BotIsPrivateError(FluxCrystalError):
    """Bot is private."""


class BotUserAuthEndpointAccessDeniedError(FluxCrystalError):
    """Access denied to bot user auth endpoint."""


class BotUserAuthSessionCreationDeniedError(FluxCrystalError):
    """Bot user auth session creation denied."""


class BotUserGenerationFailedError(FluxCrystalError):
    """Bot user generation failed."""


class BotUserNotFoundError(FluxCrystalError):
    """Bot user not found."""


# ---------------------------------------------------------------------------
# Channels & Messages
# ---------------------------------------------------------------------------

class CannotEditOtherUserMessageError(FluxCrystalError):
    """Cannot edit another user's message."""


class CannotExecuteOnDMError(FluxCrystalError):
    """Cannot execute on direct message."""


class CannotModifySystemWebhookError(FluxCrystalError):
    """Cannot modify system webhook."""


class CannotModifyVoiceStateError(FluxCrystalError):
    """Cannot modify voice state."""


class CannotSendEmptyMessageError(FluxCrystalError):
    """Cannot send empty message."""


class CannotSendMessagesInNonTextChannelError(FluxCrystalError):
    """Cannot send messages in non-text channel."""


class CannotSendMessagesToUserError(FluxCrystalError):
    """Cannot send messages to this user."""


# ---------------------------------------------------------------------------
# Channel Types
# ---------------------------------------------------------------------------

class InvalidChannelTypeError(FluxCrystalError):
    """Invalid channel type."""


class InvalidChannelTypeForCallError(FluxCrystalError):
    """Invalid channel type for call."""


# ---------------------------------------------------------------------------
# Connections
# ---------------------------------------------------------------------------

class ConnectionAlreadyExistsError(FluxCrystalError):
    """Connection already exists."""


class ConnectionInitiationTokenInvalidError(FluxCrystalError):
    """Connection initiation token is invalid."""


class ConnectionInvalidIdentifierError(FluxCrystalError):
    """Connection invalid identifier."""


class ConnectionInvalidTypeError(FluxCrystalError):
    """Connection invalid type."""


class ConnectionLimitReachedError(FluxCrystalError):
    """Connection limit reached."""


class ConnectionNotFoundError(FluxCrystalError):
    """Connection not found."""


class ConnectionVerificationFailedError(FluxCrystalError):
    """Connection verification failed."""


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

class DiscoveryAlreadyAppliedError(FluxCrystalError):
    """Discovery already applied."""


class DiscoveryApplicationAlreadyReviewedError(FluxCrystalError):
    """Discovery application already reviewed."""


class DiscoveryApplicationNotFoundError(FluxCrystalError):
    """Discovery application not found."""


class DiscoveryDescriptionRequiredError(FluxCrystalError):
    """Discovery description required."""


class DiscoveryDisabledError(FluxCrystalError):
    """Discovery is disabled."""


class DiscoveryInsufficientMembersError(FluxCrystalError):
    """Discovery insufficient members."""


class DiscoveryInvalidCategoryError(FluxCrystalError):
    """Discovery invalid category."""


class DiscoveryNotDiscoverableError(FluxCrystalError):
    """Guild is not discoverable."""


# ---------------------------------------------------------------------------
# Encryption & Security
# ---------------------------------------------------------------------------

class DecryptionFailedError(FluxCrystalError):
    """Decryption failed."""


class EncryptionFailedError(FluxCrystalError):
    """Encryption failed."""


class EmptyEncryptedBodyError(FluxCrystalError):
    """Empty encrypted body."""


class InvalidDecryptedJSONError(FluxCrystalError):
    """Invalid decrypted JSON."""


class InvalidIVError(FluxCrystalError):
    """Invalid IV (Initialization Vector)."""


class MissingIVError(FluxCrystalError):
    """Missing IV (Initialization Vector)."""


# ---------------------------------------------------------------------------
# File & Media
# ---------------------------------------------------------------------------

class FileSizeTooLargeError(FluxCrystalError):
    """File size too large."""


class InvalidStreamThumbnailPayloadError(FluxCrystalError):
    """Invalid stream thumbnail payload."""


class MediaMetadataError(FluxCrystalError):
    """Media metadata error."""


class PreviewMustBeJPEGError(FluxCrystalError):
    """Preview must be JPEG."""


class StreamThumbnailPayloadEmptyError(FluxCrystalError):
    """Stream thumbnail payload is empty."""


# ---------------------------------------------------------------------------
# Friend & Relationships
# ---------------------------------------------------------------------------

class AlreadyFriendsError(FluxCrystalError):
    """Already friends with this user."""


class BotsCannotSendFriendRequestsError(FluxCrystalError):
    """Bots cannot send friend requests."""


class CannotSendFriendRequestToBlockedUserError(FluxCrystalError):
    """Cannot send friend request to blocked user."""


class CannotSendFriendRequestToSelfError(FluxCrystalError):
    """Cannot send friend request to self."""


class FriendRequestBlockedError(FluxCrystalError):
    """Friend request blocked."""


class NotFriendsWithUserError(FluxCrystalError):
    """Not friends with this user."""


# ---------------------------------------------------------------------------
# Gateway & HTTP
# ---------------------------------------------------------------------------

class GatewayTimeoutError(FluxCrystalError):
    """Gateway timeout."""


class InternalServerError(FluxCrystalError):
    """Internal server error."""


class MethodNotAllowedError(FluxCrystalError):
    """Method not allowed."""


class ServiceUnavailableError(FluxCrystalError):
    """Service unavailable."""


# ---------------------------------------------------------------------------
# Guilds
# ---------------------------------------------------------------------------

class CannotReportOwnGuildError(FluxCrystalError):
    """Cannot report own guild."""


class CannotShrinkReservedSlotsError(FluxCrystalError):
    """Cannot shrink reserved slots."""


class GuildPhoneVerificationRequiredError(FluxCrystalError):
    """Guild phone verification required."""


class GuildVerificationRequiredError(FluxCrystalError):
    """Guild verification required."""


class UserBannedFromGuildError(FluxCrystalError):
    """User is banned from guild."""


class UserIPBannedFromGuildError(FluxCrystalError):
    """User IP is banned from guild."""


# ---------------------------------------------------------------------------
# Invites
# ---------------------------------------------------------------------------

class InvitesDisabledError(FluxCrystalError):
    """Invites are disabled."""


class UnknownInviteError(FluxCrystalError):
    """Unknown invite."""


# ---------------------------------------------------------------------------
# Members & Users
# ---------------------------------------------------------------------------

class CannotTransferOwnershipToBotError(FluxCrystalError):
    """Cannot transfer ownership to bot."""


class MissingAccessError(FluxCrystalError):
    """Missing access to the resource."""


class UnknownMemberError(FluxCrystalError):
    """Unknown member."""


class UnknownUserError(FluxCrystalError):
    """Unknown user."""


# ---------------------------------------------------------------------------
# Messages
# ---------------------------------------------------------------------------

class CannotReportOwnMessageError(FluxCrystalError):
    """Cannot report own message."""


class CannotReportYourselfError(FluxCrystalError):
    """Cannot report yourself."""


class MessageTotalAttachmentSizeTooLargeError(FluxCrystalError):
    """Message total attachment size too large."""


class UnknownMessageError(FluxCrystalError):
    """Unknown message."""


# ---------------------------------------------------------------------------
# OAuth & Tokens
# ---------------------------------------------------------------------------

class InvalidAuthTokenError(FluxCrystalError):
    """Invalid authentication token."""


class InvalidBotFlagError(FluxCrystalError):
    """Invalid bot flag."""


class InvalidClientError(FluxCrystalError):
    """Invalid client."""


class InvalidClientSecretError(FluxCrystalError):
    """Invalid client secret."""


class InvalidGrantError(FluxCrystalError):
    """Invalid grant."""


class InvalidRedirectURIError(FluxCrystalError):
    """Invalid redirect URI."""


class InvalidScopeError(FluxCrystalError):
    """Invalid scope."""


class InvalidSudoTokenError(FluxCrystalError):
    """Invalid sudo token."""


class InvalidTokenError(FluxCrystalError):
    """Invalid token."""


class MissingAuthorizationError(FluxCrystalError):
    """Missing authorization."""


class MissingOAuthAdminScopeError(FluxCrystalError):
    """Missing OAuth admin scope."""


class MissingOAuthFieldsError(FluxCrystalError):
    """Missing OAuth fields."""


class MissingOAuthScopeError(FluxCrystalError):
    """Missing OAuth scope."""


class MissingRedirectURIError(FluxCrystalError):
    """Missing redirect URI."""


class RedirectURIRequiredForNonBotError(FluxCrystalError):
    """Redirect URI required for non-bot."""


class SessionTokenMismatchError(FluxCrystalError):
    """Session token mismatch."""


class SudoModeRequiredError(FluxCrystalError):
    """Sudo mode required."""


class UnauthorizedError(FluxCrystalError):
    """Unauthorized access."""


class UnsupportedResponseTypeError(FluxCrystalError):
    """Unsupported response type."""


# ---------------------------------------------------------------------------
# Permissions
# ---------------------------------------------------------------------------

class InvalidPermissionsIntegerError(FluxCrystalError):
    """Invalid permissions integer."""


class InvalidPermissionsNegativeError(FluxCrystalError):
    """Invalid permissions – negative value."""


class MissingPermissionsError(FluxCrystalError):
    """Missing permissions."""


# ---------------------------------------------------------------------------
# Phone & Verification
# ---------------------------------------------------------------------------

class CaptchaRequiredError(FluxCrystalError):
    """Captcha required."""


class InvalidCaptchaError(FluxCrystalError):
    """Invalid captcha."""


class InvalidPhoneNumberError(FluxCrystalError):
    """Invalid phone number."""


class InvalidPhoneVerificationCodeError(FluxCrystalError):
    """Invalid phone verification code."""


class IPAuthorizationRequiredError(FluxCrystalError):
    """IP authorization required."""


class IPAuthorizationResendCooldownError(FluxCrystalError):
    """IP authorization resend cooldown."""


class IPAuthorizationResendLimitExceededError(FluxCrystalError):
    """IP authorization resend limit exceeded."""


class IPBannedError(FluxCrystalError):
    """IP banned."""


class PhoneAlreadyUsedError(FluxCrystalError):
    """Phone number already used."""


class PhoneRateLimitExceededError(FluxCrystalError):
    """Phone rate limit exceeded."""


class PhoneRequiredForSMSMFAError(FluxCrystalError):
    """Phone required for SMS MFA."""


class PhoneVerificationRequiredError(FluxCrystalError):
    """Phone verification required."""


# ---------------------------------------------------------------------------
# Subscription & Premium
# ---------------------------------------------------------------------------

class NoActiveSubscriptionError(FluxCrystalError):
    """No active subscription."""


class CannotRedeemPlutoniumWithVisionaryError(FluxCrystalError):
    """Cannot redeem plutonium with visionary."""


class NoVisionarySlotsAvailableError(FluxCrystalError):
    """No visionary slots available."""


class PremiumPurchaseBlockedError(FluxCrystalError):
    """Premium purchase blocked."""


# ---------------------------------------------------------------------------
# Two-Factor Authentication
# ---------------------------------------------------------------------------

class TwoFANotEnabledError(FluxCrystalError):
    """Two-factor authentication not enabled."""


class TwoFactorRequiredError(FluxCrystalError):
    """Two-factor authentication required."""


# ---------------------------------------------------------------------------
# Unclaimed Accounts
# ---------------------------------------------------------------------------

class UnclaimedAccountCannotAcceptFriendRequestsError(FluxCrystalError):
    """Unclaimed account cannot accept friend requests."""


class UnclaimedAccountCannotAddReactionsError(FluxCrystalError):
    """Unclaimed account cannot add reactions."""


class UnclaimedAccountCannotCreateApplicationsError(FluxCrystalError):
    """Unclaimed account cannot create applications."""


class UnclaimedAccountCannotJoinGroupDMsError(FluxCrystalError):
    """Unclaimed account cannot join group DMs."""


class UnclaimedAccountCannotJoinOneOnOneVoiceCallsError(FluxCrystalError):
    """Unclaimed account cannot join one-on-one voice calls."""


class UnclaimedAccountCannotJoinVoiceChannelsError(FluxCrystalError):
    """Unclaimed account cannot join voice channels."""


class UnclaimedAccountCannotMakePurchasesError(FluxCrystalError):
    """Unclaimed account cannot make purchases."""


class UnclaimedAccountCannotSendDirectMessagesError(FluxCrystalError):
    """Unclaimed account cannot send direct messages."""


class UnclaimedAccountCannotSendFriendRequestsError(FluxCrystalError):
    """Unclaimed account cannot send friend requests."""


class UnclaimedAccountCannotSendMessagesError(FluxCrystalError):
    """Unclaimed account cannot send messages."""


# ---------------------------------------------------------------------------
# Unknown / Not Found
# ---------------------------------------------------------------------------

class UnknownChannelError(FluxCrystalError):
    """Unknown channel."""


class UnknownEmojiError(FluxCrystalError):
    """Unknown emoji."""


class UnknownFavoriteMemeError(FluxCrystalError):
    """Unknown favorite meme."""


class UnknownGiftCodeError(FluxCrystalError):
    """Unknown gift code."""


class UnknownGuildError(FluxCrystalError):
    """Unknown guild."""


class UnknownHarvestError(FluxCrystalError):
    """Unknown harvest."""


class UnknownPackError(FluxCrystalError):
    """Unknown pack."""


class UnknownReportError(FluxCrystalError):
    """Unknown report."""


class UnknownRoleError(FluxCrystalError):
    """Unknown role."""


class UnknownStickerError(FluxCrystalError):
    """Unknown sticker."""


class UnknownSuspiciousFlagError(FluxCrystalError):
    """Unknown suspicious flag."""


class UnknownUserFlagError(FluxCrystalError):
    """Unknown user flag."""


class UnknownVoiceRegionError(FluxCrystalError):
    """Unknown voice region."""


class UnknownVoiceServerError(FluxCrystalError):
    """Unknown voice server."""


class UnknownApplicationError(FluxCrystalError):
    """Unknown application."""


class UnknownWebhookError(FluxCrystalError):
    """Unknown webhook."""


class UnknownWebAuthnCredentialError(FluxCrystalError):
    """Unknown WebAuthn credential."""


# ---------------------------------------------------------------------------
# Voice & Calls
# ---------------------------------------------------------------------------

class CallAlreadyExistsError(FluxCrystalError):
    """Call already exists."""


class NoActiveCallError(FluxCrystalError):
    """No active call."""


class NotInVoiceError(FluxCrystalError):
    """User not in voice."""


class VoiceChannelFullError(FluxCrystalError):
    """Voice channel is full."""


# ---------------------------------------------------------------------------
# WebAuthn
# ---------------------------------------------------------------------------

class InvalidWebAuthnAuthenticationCounterError(FluxCrystalError):
    """Invalid WebAuthn authentication counter."""


class InvalidWebAuthnCredentialCounterError(FluxCrystalError):
    """Invalid WebAuthn credential counter."""


class InvalidWebAuthnCredentialError(FluxCrystalError):
    """Invalid WebAuthn credential."""


class InvalidWebAuthnPublicKeyFormatError(FluxCrystalError):
    """Invalid WebAuthn public key format."""


class NoPasskeysRegisteredError(FluxCrystalError):
    """No passkeys registered."""


class PasskeyAuthenticationFailedError(FluxCrystalError):
    """Passkey authentication failed."""


class PasskeysDisabledError(FluxCrystalError):
    """Passkeys are disabled."""


class WebAuthnCredentialLimitReachedError(FluxCrystalError):
    """WebAuthn credential limit reached."""


# ---------------------------------------------------------------------------
# Rate Limiting
# ---------------------------------------------------------------------------

class RateLimitedError(FluxCrystalError):
    """Rate limited."""

    def __init__(self, message: str, retry_after: float = 0.0) -> None:
        super().__init__(message)
        #: Seconds to wait before retrying, if provided by the server.
        self.retry_after: float = retry_after


class SlowmodeRateLimitedError(FluxCrystalError):
    """Slowmode rate limited."""


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

class ConflictError(FluxCrystalError):
    """Conflict."""


class ContentBlockedError(FluxCrystalError):
    """Content blocked."""


class ExplicitContentCannotBeSentError(FluxCrystalError):
    """Explicit content cannot be sent."""


class ForbiddenError(FluxCrystalError):
    """Forbidden."""


class GeneralError(FluxCrystalError):
    """General error."""


class GoneError(FluxCrystalError):
    """Resource gone."""


class InvalidFormBodyError(FluxCrystalError):
    """Invalid form body."""


class InvalidRequestError(FluxCrystalError):
    """Invalid request."""


class NotFoundError(FluxCrystalError):
    """Not found."""


class NotImplementedAPIError(FluxCrystalError):
    """API endpoint not implemented."""


class ResponseValidationError(FluxCrystalError):
    """Response validation error."""


class ValidationError(FluxCrystalError):
    """Validation error."""


# ---------------------------------------------------------------------------
# Feature-Specific
# ---------------------------------------------------------------------------

class FeatureNotAvailableSelfHostedError(FluxCrystalError):
    """Feature not available on self-hosted instance."""


class FeatureTemporarilyDisabledError(FluxCrystalError):
    """Feature temporarily disabled."""


class HTTPGetAuthorizeNotSupportedError(FluxCrystalError):
    """HTTP GET authorize not supported."""


class InstanceVersionMismatchError(FluxCrystalError):
    """Instance version mismatch."""


# ---------------------------------------------------------------------------
# Harvest
# ---------------------------------------------------------------------------

class HarvestExpiredError(FluxCrystalError):
    """Harvest expired."""


class HarvestFailedError(FluxCrystalError):
    """Harvest failed."""


class HarvestNotReadyError(FluxCrystalError):
    """Harvest not ready."""


class HarvestOnCooldownError(FluxCrystalError):
    """Harvest on cooldown."""


# ---------------------------------------------------------------------------
# Miscellaneous
# ---------------------------------------------------------------------------

class AuditLogIndexingError(FluxCrystalError):
    """Audit log indexing error."""


class ChannelIndexingError(FluxCrystalError):
    """Channel indexing error."""


class CommunicationDisabledError(FluxCrystalError):
    """Communication disabled."""


class CreationFailedError(FluxCrystalError):
    """Creation failed."""


class CSAMScanFailedError(FluxCrystalError):
    """CSAM scan failed."""


class CSAMScanParseError(FluxCrystalError):
    """CSAM scan parse error."""


class CSAMScanSubscriptionError(FluxCrystalError):
    """CSAM scan subscription error."""


class CSAMScanTimeoutError(FluxCrystalError):
    """CSAM scan timeout."""


class DeletionFailedError(FluxCrystalError):
    """Deletion failed."""


class DiscriminatorRequiredError(FluxCrystalError):
    """Discriminator required."""


class EmailServiceNotTestableError(FluxCrystalError):
    """Email service not testable."""


class EmailVerificationRequiredError(FluxCrystalError):
    """Email verification required."""


class GiftCodeAlreadyRedeemedError(FluxCrystalError):
    """Gift code already redeemed."""


class HandoffCodeExpiredError(FluxCrystalError):
    """Handoff code expired."""


class InvalidDSAReportTargetError(FluxCrystalError):
    """Invalid DSA report target."""


class InvalidDSATicketError(FluxCrystalError):
    """Invalid DSA ticket."""


class InvalidDSAVerificationCodeError(FluxCrystalError):
    """Invalid DSA verification code."""


class InvalidEphemeralKeyError(FluxCrystalError):
    """Invalid ephemeral key."""


class InvalidFlagsFormatError(FluxCrystalError):
    """Invalid flags format."""


class InvalidHandOffCodeError(FluxCrystalError):
    """Invalid handoff code."""


class InvalidPackTypeError(FluxCrystalError):
    """Invalid pack type."""


class InvalidResponseTypeForNonBotError(FluxCrystalError):
    """Invalid response type for non-bot."""


class InvalidStreamKeyFormatError(FluxCrystalError):
    """Invalid stream key format."""


class InvalidSuspiciousFlagsFormatError(FluxCrystalError):
    """Invalid suspicious flags format."""


class InvalidSystemFlagError(FluxCrystalError):
    """Invalid system flag."""


class InvalidTimestampError(FluxCrystalError):
    """Invalid timestamp."""


class MissingClientSecretError(FluxCrystalError):
    """Missing client secret."""


class MissingEphemeralKeyError(FluxCrystalError):
    """Missing ephemeral key."""


class NCMECAlreadySubmittedError(FluxCrystalError):
    """NCMEC already submitted."""


class NCMECSubmissionFailedError(FluxCrystalError):
    """NCMEC submission failed."""


class NoPendingDeletionError(FluxCrystalError):
    """No pending deletion."""


class NoUsersWithFluxertagExistError(FluxCrystalError):
    """No users with Fluxertag exist."""


class NSFWContentAgeRestrictedError(FluxCrystalError):
    """NSFW content age restricted."""


class PackAccessDeniedError(FluxCrystalError):
    """Pack access denied."""


class ProcessingFailedError(FluxCrystalError):
    """Processing failed."""


class ReportAlreadyResolvedError(FluxCrystalError):
    """Report already resolved."""


class ReportBannedError(FluxCrystalError):
    """Report banned."""


class SSORequiredError(FluxCrystalError):
    """SSO required."""


class StreamKeyChannelMismatchError(FluxCrystalError):
    """Stream key channel mismatch."""


class StreamKeyScopeMismatchError(FluxCrystalError):
    """Stream key scope mismatch."""


class TagAlreadyTakenError(FluxCrystalError):
    """Tag already taken."""


class TemporaryInviteRequiresPresenceError(FluxCrystalError):
    """Temporary invite requires presence."""


class TestHarnessDisabledError(FluxCrystalError):
    """Test harness disabled."""


class TestHarnessForbiddenError(FluxCrystalError):
    """Test harness forbidden."""


class UpdateFailedError(FluxCrystalError):
    """Update failed."""


class UserOwnsGuildsError(FluxCrystalError):
    """User owns guilds."""


# ---------------------------------------------------------------------------
# Stripe / Payments
# ---------------------------------------------------------------------------

class StripeError(FluxCrystalError):
    """Stripe error."""


class StripeGiftRedemptionInProgressError(FluxCrystalError):
    """Stripe gift redemption in progress."""


class StripeInvalidProductError(FluxCrystalError):
    """Stripe invalid product."""


class StripeInvalidProductConfigurationError(FluxCrystalError):
    """Stripe invalid product configuration."""


class StripeNoActiveSubscriptionError(FluxCrystalError):
    """Stripe no active subscription."""


class StripeNoPurchaseHistoryError(FluxCrystalError):
    """Stripe no purchase history."""


class StripeNoSubscriptionError(FluxCrystalError):
    """Stripe no subscription."""


class StripePaymentNotAvailableError(FluxCrystalError):
    """Stripe payment not available."""


class StripeSubscriptionAlreadyCancelingError(FluxCrystalError):
    """Stripe subscription already canceling."""


class StripeSubscriptionNotCancelingError(FluxCrystalError):
    """Stripe subscription not canceling."""


class StripeSubscriptionPeriodEndMissingError(FluxCrystalError):
    """Stripe subscription period end missing."""


class StripeWebhookNotAvailableError(FluxCrystalError):
    """Stripe webhook not available."""


class StripeWebhookSignatureInvalidError(FluxCrystalError):
    """Stripe webhook signature invalid."""


class StripeWebhookSignatureMissingError(FluxCrystalError):
    """Stripe webhook signature missing."""


# ---------------------------------------------------------------------------
# Donations
# ---------------------------------------------------------------------------

class DonationAmountInvalidError(FluxCrystalError):
    """Donation amount invalid."""


class DonationMagicLinkExpiredError(FluxCrystalError):
    """Donation magic link expired."""


class DonationMagicLinkInvalidError(FluxCrystalError):
    """Donation magic link invalid."""


class DonationMagicLinkUsedError(FluxCrystalError):
    """Donation magic link used."""


class DonorNotFoundError(FluxCrystalError):
    """Donor not found."""


# ---------------------------------------------------------------------------
# MFA
# ---------------------------------------------------------------------------

class SMSMFANotEnabledError(FluxCrystalError):
    """SMS MFA not enabled."""


class SMSMFARequiresTOTPError(FluxCrystalError):
    """SMS MFA requires TOTP."""


class SMSVerificationUnavailableError(FluxCrystalError):
    """SMS verification unavailable."""


# ---------------------------------------------------------------------------
# Max Limits
# ---------------------------------------------------------------------------

class MaxAnimatedEmojisError(FluxCrystalError):
    """Maximum animated emojis reached."""


class MaxBookmarksError(FluxCrystalError):
    """Maximum bookmarks reached."""


class MaxCategoryChannelsError(FluxCrystalError):
    """Maximum category channels reached."""


class MaxEmojisError(FluxCrystalError):
    """Maximum emojis reached."""


class MaxFavoriteMemesError(FluxCrystalError):
    """Maximum favorite memes reached."""


class MaxFriendsError(FluxCrystalError):
    """Maximum friends reached."""


class MaxGroupDMRecipientsError(FluxCrystalError):
    """Maximum group DM recipients reached."""


class MaxGroupDMsError(FluxCrystalError):
    """Maximum group DMs reached."""


class MaxGuildChannelsError(FluxCrystalError):
    """Maximum guild channels reached."""


class MaxGuildMembersError(FluxCrystalError):
    """Maximum guild members reached."""


class MaxGuildRolesError(FluxCrystalError):
    """Maximum guild roles reached."""


class MaxGuildsError(FluxCrystalError):
    """Maximum guilds reached."""


class MaxInvitesError(FluxCrystalError):
    """Maximum invites reached."""


class MaxPackExpressionsError(FluxCrystalError):
    """Maximum pack expressions reached."""


class MaxPacksError(FluxCrystalError):
    """Maximum packs reached."""


class MaxPinsPerChannelError(FluxCrystalError):
    """Maximum pins per channel reached."""


class MaxReactionsError(FluxCrystalError):
    """Maximum reactions reached."""


class MaxStickersError(FluxCrystalError):
    """Maximum stickers reached."""


class MaxWebhooksPerChannelError(FluxCrystalError):
    """Maximum webhooks per channel reached."""


class MaxWebhooksPerGuildError(FluxCrystalError):
    """Maximum webhooks per guild reached."""


class MaxWebhooksError(FluxCrystalError):
    """Maximum webhooks reached."""


# ---------------------------------------------------------------------------
# Usernames
# ---------------------------------------------------------------------------

class UsernameNotAvailableError(FluxCrystalError):
    """Username not available."""


# ---------------------------------------------------------------------------
# Error code → exception class mapping
# ---------------------------------------------------------------------------

ERROR_CODE_MAPPING: dict[str, type[FluxCrystalError]] = {
    "ACCESS_DENIED": AccessDeniedError,
    "ACCOUNT_DISABLED": AccountDisabledError,
    "BAD_GATEWAY": BadGatewayError,
    "BAD_REQUEST": BadRequestError,
    "BLUESKY_OAUTH_AUTHORIZATION_FAILED": BlueskyOAuthAuthorizationFailedError,
    "BLUESKY_OAUTH_CALLBACK_FAILED": BlueskyOAuthCallbackFailedError,
    "BLUESKY_OAUTH_NOT_ENABLED": BlueskyOAuthNotEnabledError,
    "BLUESKY_OAUTH_SESSION_EXPIRED": BlueskyOAuthSessionExpiredError,
    "BLUESKY_OAUTH_STATE_INVALID": BlueskyOAuthStateInvalidError,
    "ACCOUNT_SCHEDULED_FOR_DELETION": AccountScheduledForDeletionError,
    "ACCOUNT_SUSPENDED_PERMANENTLY": AccountSuspendedPermanentlyError,
    "ACCOUNT_SUSPENDED_TEMPORARILY": AccountSuspendedTemporarilyError,
    "ACCOUNT_SUSPICIOUS_ACTIVITY": AccountSuspiciousActivityError,
    "ACCOUNT_TOO_NEW_FOR_GUILD": AccountTooNewForGuildError,
    "ACLS_MUST_BE_NON_EMPTY": ACLsMustBeNonEmptyError,
    "ADMIN_API_KEY_NOT_FOUND": AdminAPIKeyNotFoundError,
    "APPLICATION_NOT_FOUND": ApplicationNotFoundError,
    "APPLICATION_NOT_OWNED": ApplicationNotOwnedError,
    "ALREADY_FRIENDS": AlreadyFriendsError,
    "AUDIT_LOG_INDEXING": AuditLogIndexingError,
    "BOTS_CANNOT_SEND_FRIEND_REQUESTS": BotsCannotSendFriendRequestsError,
    "BOT_ALREADY_IN_GUILD": BotAlreadyInGuildError,
    "BOT_APPLICATION_NOT_FOUND": BotApplicationNotFoundError,
    "BOT_IS_PRIVATE": BotIsPrivateError,
    "BOT_USER_AUTH_ENDPOINT_ACCESS_DENIED": BotUserAuthEndpointAccessDeniedError,
    "BOT_USER_AUTH_SESSION_CREATION_DENIED": BotUserAuthSessionCreationDeniedError,
    "BOT_USER_GENERATION_FAILED": BotUserGenerationFailedError,
    "BOT_USER_NOT_FOUND": BotUserNotFoundError,
    "CALL_ALREADY_EXISTS": CallAlreadyExistsError,
    "CANNOT_EDIT_OTHER_USER_MESSAGE": CannotEditOtherUserMessageError,
    "CANNOT_EXECUTE_ON_DM": CannotExecuteOnDMError,
    "CANNOT_MODIFY_SYSTEM_WEBHOOK": CannotModifySystemWebhookError,
    "CANNOT_MODIFY_VOICE_STATE": CannotModifyVoiceStateError,
    "CANNOT_REDEEM_PLUTONIUM_WITH_VISIONARY": CannotRedeemPlutoniumWithVisionaryError,
    "CANNOT_REPORT_OWN_GUILD": CannotReportOwnGuildError,
    "CANNOT_REPORT_OWN_MESSAGE": CannotReportOwnMessageError,
    "CANNOT_REPORT_YOURSELF": CannotReportYourselfError,
    "CANNOT_SEND_EMPTY_MESSAGE": CannotSendEmptyMessageError,
    "CANNOT_SEND_FRIEND_REQUEST_TO_BLOCKED_USER": CannotSendFriendRequestToBlockedUserError,
    "CANNOT_SEND_FRIEND_REQUEST_TO_SELF": CannotSendFriendRequestToSelfError,
    "CANNOT_SEND_MESSAGES_IN_NON_TEXT_CHANNEL": CannotSendMessagesInNonTextChannelError,
    "CANNOT_SEND_MESSAGES_TO_USER": CannotSendMessagesToUserError,
    "CANNOT_TRANSFER_OWNERSHIP_TO_BOT": CannotTransferOwnershipToBotError,
    "CANNOT_SHRINK_RESERVED_SLOTS": CannotShrinkReservedSlotsError,
    "CAPTCHA_REQUIRED": CaptchaRequiredError,
    "CHANNEL_INDEXING": ChannelIndexingError,
    "COMMUNICATION_DISABLED": CommunicationDisabledError,
    "CONNECTION_ALREADY_EXISTS": ConnectionAlreadyExistsError,
    "CONNECTION_INITIATION_TOKEN_INVALID": ConnectionInitiationTokenInvalidError,
    "CONNECTION_INVALID_IDENTIFIER": ConnectionInvalidIdentifierError,
    "CONNECTION_INVALID_TYPE": ConnectionInvalidTypeError,
    "CONNECTION_LIMIT_REACHED": ConnectionLimitReachedError,
    "CONNECTION_NOT_FOUND": ConnectionNotFoundError,
    "CONNECTION_VERIFICATION_FAILED": ConnectionVerificationFailedError,
    "CONFLICT": ConflictError,
    "CONTENT_BLOCKED": ContentBlockedError,
    "CREATION_FAILED": CreationFailedError,
    "CSAM_SCAN_FAILED": CSAMScanFailedError,
    "CSAM_SCAN_PARSE_ERROR": CSAMScanParseError,
    "CSAM_SCAN_SUBSCRIPTION_ERROR": CSAMScanSubscriptionError,
    "CSAM_SCAN_TIMEOUT": CSAMScanTimeoutError,
    "DECRYPTION_FAILED": DecryptionFailedError,
    "DELETION_FAILED": DeletionFailedError,
    "DISCOVERY_ALREADY_APPLIED": DiscoveryAlreadyAppliedError,
    "DISCOVERY_APPLICATION_ALREADY_REVIEWED": DiscoveryApplicationAlreadyReviewedError,
    "DISCOVERY_APPLICATION_NOT_FOUND": DiscoveryApplicationNotFoundError,
    "DISCOVERY_DESCRIPTION_REQUIRED": DiscoveryDescriptionRequiredError,
    "DISCOVERY_DISABLED": DiscoveryDisabledError,
    "DISCOVERY_INSUFFICIENT_MEMBERS": DiscoveryInsufficientMembersError,
    "DISCOVERY_INVALID_CATEGORY": DiscoveryInvalidCategoryError,
    "DISCOVERY_NOT_DISCOVERABLE": DiscoveryNotDiscoverableError,
    "DISCRIMINATOR_REQUIRED": DiscriminatorRequiredError,
    "EMAIL_SERVICE_NOT_TESTABLE": EmailServiceNotTestableError,
    "EMAIL_VERIFICATION_REQUIRED": EmailVerificationRequiredError,
    "EMPTY_ENCRYPTED_BODY": EmptyEncryptedBodyError,
    "ENCRYPTION_FAILED": EncryptionFailedError,
    "EXPLICIT_CONTENT_CANNOT_BE_SENT": ExplicitContentCannotBeSentError,
    "FEATURE_NOT_AVAILABLE_SELF_HOSTED": FeatureNotAvailableSelfHostedError,
    "FEATURE_TEMPORARILY_DISABLED": FeatureTemporarilyDisabledError,
    "FILE_SIZE_TOO_LARGE": FileSizeTooLargeError,
    "FORBIDDEN": ForbiddenError,
    "FRIEND_REQUEST_BLOCKED": FriendRequestBlockedError,
    "GATEWAY_TIMEOUT": GatewayTimeoutError,
    "GENERAL_ERROR": GeneralError,
    "GONE": GoneError,
    "GIFT_CODE_ALREADY_REDEEMED": GiftCodeAlreadyRedeemedError,
    "GUILD_PHONE_VERIFICATION_REQUIRED": GuildPhoneVerificationRequiredError,
    "GUILD_VERIFICATION_REQUIRED": GuildVerificationRequiredError,
    "HANDOFF_CODE_EXPIRED": HandoffCodeExpiredError,
    "HARVEST_EXPIRED": HarvestExpiredError,
    "HARVEST_FAILED": HarvestFailedError,
    "HARVEST_NOT_READY": HarvestNotReadyError,
    "HARVEST_ON_COOLDOWN": HarvestOnCooldownError,
    "HTTP_GET_AUTHORIZE_NOT_SUPPORTED": HTTPGetAuthorizeNotSupportedError,
    "INSTANCE_VERSION_MISMATCH": InstanceVersionMismatchError,
    "INTERNAL_SERVER_ERROR": InternalServerError,
    "INVALID_ACLS_FORMAT": InvalidACLsFormatError,
    "INVALID_API_ORIGIN": InvalidFormBodyError,
    "INVALID_AUTH_TOKEN": InvalidAuthTokenError,
    "INVALID_BOT_FLAG": InvalidBotFlagError,
    "INVALID_CAPTCHA": InvalidCaptchaError,
    "INVALID_CHANNEL_TYPE_FOR_CALL": InvalidChannelTypeForCallError,
    "INVALID_CHANNEL_TYPE": InvalidChannelTypeError,
    "INVALID_CLIENT": InvalidClientError,
    "INVALID_CLIENT_SECRET": InvalidClientSecretError,
    "INVALID_DSA_REPORT_TARGET": InvalidDSAReportTargetError,
    "INVALID_DSA_TICKET": InvalidDSATicketError,
    "INVALID_DSA_VERIFICATION_CODE": InvalidDSAVerificationCodeError,
    "INVALID_DECRYPTED_JSON": InvalidDecryptedJSONError,
    "INVALID_EPHEMERAL_KEY": InvalidEphemeralKeyError,
    "INVALID_FLAGS_FORMAT": InvalidFlagsFormatError,
    "INVALID_IV": InvalidIVError,
    "INVALID_FORM_BODY": InvalidFormBodyError,
    "INVALID_GRANT": InvalidGrantError,
    "INVALID_HANDOFF_CODE": InvalidHandOffCodeError,
    "INVALID_PACK_TYPE": InvalidPackTypeError,
    "INVALID_PERMISSIONS_INTEGER": InvalidPermissionsIntegerError,
    "INVALID_PERMISSIONS_NEGATIVE": InvalidPermissionsNegativeError,
    "INVALID_PHONE_NUMBER": InvalidPhoneNumberError,
    "INVALID_PHONE_VERIFICATION_CODE": InvalidPhoneVerificationCodeError,
    "INVALID_REDIRECT_URI": InvalidRedirectURIError,
    "INVALID_REQUEST": InvalidRequestError,
    "INVALID_RESPONSE_TYPE_FOR_NON_BOT": InvalidResponseTypeForNonBotError,
    "INVALID_SCOPE": InvalidScopeError,
    "INVALID_STREAM_KEY_FORMAT": InvalidStreamKeyFormatError,
    "INVALID_STREAM_THUMBNAIL_PAYLOAD": InvalidStreamThumbnailPayloadError,
    "INVALID_SUDO_TOKEN": InvalidSudoTokenError,
    "INVALID_SUSPICIOUS_FLAGS_FORMAT": InvalidSuspiciousFlagsFormatError,
    "INVALID_SYSTEM_FLAG": InvalidSystemFlagError,
    "INVALID_TIMESTAMP": InvalidTimestampError,
    "INVALID_TOKEN": InvalidTokenError,
    "INVALID_WEBAUTHN_AUTHENTICATION_COUNTER": InvalidWebAuthnAuthenticationCounterError,
    "INVALID_WEBAUTHN_CREDENTIAL_COUNTER": InvalidWebAuthnCredentialCounterError,
    "INVALID_WEBAUTHN_CREDENTIAL": InvalidWebAuthnCredentialError,
    "INVALID_WEBAUTHN_PUBLIC_KEY_FORMAT": InvalidWebAuthnPublicKeyFormatError,
    "INVITES_DISABLED": InvitesDisabledError,
    "IP_AUTHORIZATION_REQUIRED": IPAuthorizationRequiredError,
    "IP_AUTHORIZATION_RESEND_COOLDOWN": IPAuthorizationResendCooldownError,
    "IP_AUTHORIZATION_RESEND_LIMIT_EXCEEDED": IPAuthorizationResendLimitExceededError,
    "IP_BANNED": IPBannedError,
    "MAX_ANIMATED_EMOJIS": MaxAnimatedEmojisError,
    "MAX_BOOKMARKS": MaxBookmarksError,
    "MAX_CATEGORY_CHANNELS": MaxCategoryChannelsError,
    "MAX_EMOJIS": MaxEmojisError,
    "MAX_FAVORITE_MEMES": MaxFavoriteMemesError,
    "MAX_FRIENDS": MaxFriendsError,
    "MAX_GROUP_DM_RECIPIENTS": MaxGroupDMRecipientsError,
    "MAX_GROUP_DMS": MaxGroupDMsError,
    "MAX_GUILD_CHANNELS": MaxGuildChannelsError,
    "MAX_GUILD_MEMBERS": MaxGuildMembersError,
    "MAX_GUILD_ROLES": MaxGuildRolesError,
    "MAX_GUILDS": MaxGuildsError,
    "MAX_INVITES": MaxInvitesError,
    "MAX_PACK_EXPRESSIONS": MaxPackExpressionsError,
    "MAX_PACKS": MaxPacksError,
    "MAX_PINS_PER_CHANNEL": MaxPinsPerChannelError,
    "MESSAGE_TOTAL_ATTACHMENT_SIZE_TOO_LARGE": MessageTotalAttachmentSizeTooLargeError,
    "MAX_REACTIONS": MaxReactionsError,
    "MAX_STICKERS": MaxStickersError,
    "MAX_WEBHOOKS_PER_CHANNEL": MaxWebhooksPerChannelError,
    "MAX_WEBHOOKS_PER_GUILD": MaxWebhooksPerGuildError,
    "MAX_WEBHOOKS": MaxWebhooksError,
    "NCMEC_ALREADY_SUBMITTED": NCMECAlreadySubmittedError,
    "NCMEC_SUBMISSION_FAILED": NCMECSubmissionFailedError,
    "MEDIA_METADATA_ERROR": MediaMetadataError,
    "METHOD_NOT_ALLOWED": MethodNotAllowedError,
    "MISSING_ACCESS": MissingAccessError,
    "MISSING_ACL": MissingACLError,
    "MISSING_AUTHORIZATION": MissingAuthorizationError,
    "MISSING_CLIENT_SECRET": MissingClientSecretError,
    "MISSING_EPHEMERAL_KEY": MissingEphemeralKeyError,
    "MISSING_IV": MissingIVError,
    "MISSING_OAUTH_ADMIN_SCOPE": MissingOAuthAdminScopeError,
    "MISSING_OAUTH_FIELDS": MissingOAuthFieldsError,
    "MISSING_OAUTH_SCOPE": MissingOAuthScopeError,
    "MISSING_PERMISSIONS": MissingPermissionsError,
    "MISSING_REDIRECT_URI": MissingRedirectURIError,
    "NO_ACTIVE_CALL": NoActiveCallError,
    "NO_ACTIVE_SUBSCRIPTION": NoActiveSubscriptionError,
    "NOT_FOUND": NotFoundError,
    "NOT_IMPLEMENTED": NotImplementedAPIError,
    "NO_PASSKEYS_REGISTERED": NoPasskeysRegisteredError,
    "NO_PENDING_DELETION": NoPendingDeletionError,
    "NO_USERS_WITH_FLUXERTAG_EXIST": NoUsersWithFluxertagExistError,
    "NO_VISIONARY_SLOTS_AVAILABLE": NoVisionarySlotsAvailableError,
    "NOT_A_BOT_APPLICATION": NotABotApplicationError,
    "NOT_FRIENDS_WITH_USER": NotFriendsWithUserError,
    "NOT_OWNER_OF_ADMIN_API_KEY": NotOwnerOfAdminAPIKeyError,
    "NSFW_CONTENT_AGE_RESTRICTED": NSFWContentAgeRestrictedError,
    "PACK_ACCESS_DENIED": PackAccessDeniedError,
    "PASSKEY_AUTHENTICATION_FAILED": PasskeyAuthenticationFailedError,
    "PASSKEYS_DISABLED": PasskeysDisabledError,
    "PHONE_ALREADY_USED": PhoneAlreadyUsedError,
    "PHONE_RATE_LIMIT_EXCEEDED": PhoneRateLimitExceededError,
    "PHONE_REQUIRED_FOR_SMS_MFA": PhoneRequiredForSMSMFAError,
    "PHONE_VERIFICATION_REQUIRED": PhoneVerificationRequiredError,
    "PREMIUM_PURCHASE_BLOCKED": PremiumPurchaseBlockedError,
    "PREVIEW_MUST_BE_JPEG": PreviewMustBeJPEGError,
    "PROCESSING_FAILED": ProcessingFailedError,
    "RATE_LIMITED": RateLimitedError,
    "REDIRECT_URI_REQUIRED_FOR_NON_BOT": RedirectURIRequiredForNonBotError,
    "REPORT_ALREADY_RESOLVED": ReportAlreadyResolvedError,
    "REPORT_BANNED": ReportBannedError,
    "RESPONSE_VALIDATION_ERROR": ResponseValidationError,
    "SERVICE_UNAVAILABLE": ServiceUnavailableError,
    "SESSION_TOKEN_MISMATCH": SessionTokenMismatchError,
    "SLOWMODE_RATE_LIMITED": SlowmodeRateLimitedError,
    "SMS_MFA_NOT_ENABLED": SMSMFANotEnabledError,
    "SMS_MFA_REQUIRES_TOTP": SMSMFARequiresTOTPError,
    "SMS_VERIFICATION_UNAVAILABLE": SMSVerificationUnavailableError,
    "SSO_REQUIRED": SSORequiredError,
    "STREAM_KEY_CHANNEL_MISMATCH": StreamKeyChannelMismatchError,
    "STREAM_KEY_SCOPE_MISMATCH": StreamKeyScopeMismatchError,
    "STREAM_THUMBNAIL_PAYLOAD_EMPTY": StreamThumbnailPayloadEmptyError,
    "STRIPE_ERROR": StripeError,
    "STRIPE_GIFT_REDEMPTION_IN_PROGRESS": StripeGiftRedemptionInProgressError,
    "STRIPE_INVALID_PRODUCT": StripeInvalidProductError,
    "STRIPE_INVALID_PRODUCT_CONFIGURATION": StripeInvalidProductConfigurationError,
    "STRIPE_NO_ACTIVE_SUBSCRIPTION": StripeNoActiveSubscriptionError,
    "STRIPE_NO_PURCHASE_HISTORY": StripeNoPurchaseHistoryError,
    "STRIPE_NO_SUBSCRIPTION": StripeNoSubscriptionError,
    "STRIPE_PAYMENT_NOT_AVAILABLE": StripePaymentNotAvailableError,
    "STRIPE_SUBSCRIPTION_ALREADY_CANCELING": StripeSubscriptionAlreadyCancelingError,
    "STRIPE_SUBSCRIPTION_NOT_CANCELING": StripeSubscriptionNotCancelingError,
    "STRIPE_SUBSCRIPTION_PERIOD_END_MISSING": StripeSubscriptionPeriodEndMissingError,
    "STRIPE_WEBHOOK_NOT_AVAILABLE": StripeWebhookNotAvailableError,
    "STRIPE_WEBHOOK_SIGNATURE_INVALID": StripeWebhookSignatureInvalidError,
    "STRIPE_WEBHOOK_SIGNATURE_MISSING": StripeWebhookSignatureMissingError,
    "DONATION_AMOUNT_INVALID": DonationAmountInvalidError,
    "DONATION_MAGIC_LINK_EXPIRED": DonationMagicLinkExpiredError,
    "DONATION_MAGIC_LINK_INVALID": DonationMagicLinkInvalidError,
    "DONATION_MAGIC_LINK_USED": DonationMagicLinkUsedError,
    "DONOR_NOT_FOUND": DonorNotFoundError,
    "SUDO_MODE_REQUIRED": SudoModeRequiredError,
    "TAG_ALREADY_TAKEN": TagAlreadyTakenError,
    "TEMPORARY_INVITE_REQUIRES_PRESENCE": TemporaryInviteRequiresPresenceError,
    "TEST_HARNESS_DISABLED": TestHarnessDisabledError,
    "TEST_HARNESS_FORBIDDEN": TestHarnessForbiddenError,
    "TWO_FA_NOT_ENABLED": TwoFANotEnabledError,
    "TWO_FACTOR_REQUIRED": TwoFactorRequiredError,
    "UNAUTHORIZED": UnauthorizedError,
    "UNCLAIMED_ACCOUNT_CANNOT_ACCEPT_FRIEND_REQUESTS": UnclaimedAccountCannotAcceptFriendRequestsError,
    "UNCLAIMED_ACCOUNT_CANNOT_ADD_REACTIONS": UnclaimedAccountCannotAddReactionsError,
    "UNCLAIMED_ACCOUNT_CANNOT_CREATE_APPLICATIONS": UnclaimedAccountCannotCreateApplicationsError,
    "UNCLAIMED_ACCOUNT_CANNOT_JOIN_GROUP_DMS": UnclaimedAccountCannotJoinGroupDMsError,
    "UNCLAIMED_ACCOUNT_CANNOT_JOIN_ONE_ON_ONE_VOICE_CALLS": UnclaimedAccountCannotJoinOneOnOneVoiceCallsError,
    "UNCLAIMED_ACCOUNT_CANNOT_JOIN_VOICE_CHANNELS": UnclaimedAccountCannotJoinVoiceChannelsError,
    "UNCLAIMED_ACCOUNT_CANNOT_MAKE_PURCHASES": UnclaimedAccountCannotMakePurchasesError,
    "UNCLAIMED_ACCOUNT_CANNOT_SEND_DIRECT_MESSAGES": UnclaimedAccountCannotSendDirectMessagesError,
    "UNCLAIMED_ACCOUNT_CANNOT_SEND_FRIEND_REQUESTS": UnclaimedAccountCannotSendFriendRequestsError,
    "UNCLAIMED_ACCOUNT_CANNOT_SEND_MESSAGES": UnclaimedAccountCannotSendMessagesError,
    "UNKNOWN_CHANNEL": UnknownChannelError,
    "UNKNOWN_EMOJI": UnknownEmojiError,
    "UNKNOWN_FAVORITE_MEME": UnknownFavoriteMemeError,
    "UNKNOWN_GIFT_CODE": UnknownGiftCodeError,
    "UNKNOWN_GUILD": UnknownGuildError,
    "UNKNOWN_HARVEST": UnknownHarvestError,
    "UNKNOWN_INVITE": UnknownInviteError,
    "UNKNOWN_MEMBER": UnknownMemberError,
    "UNKNOWN_MESSAGE": UnknownMessageError,
    "UNKNOWN_PACK": UnknownPackError,
    "UNKNOWN_REPORT": UnknownReportError,
    "UNKNOWN_ROLE": UnknownRoleError,
    "UNKNOWN_STICKER": UnknownStickerError,
    "UNKNOWN_SUSPICIOUS_FLAG": UnknownSuspiciousFlagError,
    "UNKNOWN_USER_FLAG": UnknownUserFlagError,
    "UNKNOWN_USER": UnknownUserError,
    "UNKNOWN_VOICE_REGION": UnknownVoiceRegionError,
    "UNKNOWN_VOICE_SERVER": UnknownVoiceServerError,
    "UNKNOWN_WEBAUTHN_CREDENTIAL": UnknownWebAuthnCredentialError,
    "UNKNOWN_APPLICATION": UnknownApplicationError,
    "UNKNOWN_WEBHOOK": UnknownWebhookError,
    "UNSUPPORTED_RESPONSE_TYPE": UnsupportedResponseTypeError,
    "USERNAME_NOT_AVAILABLE": UsernameNotAvailableError,
    "UPDATE_FAILED": UpdateFailedError,
    "USER_BANNED_FROM_GUILD": UserBannedFromGuildError,
    "USER_IP_BANNED_FROM_GUILD": UserIPBannedFromGuildError,
    "USER_NOT_IN_VOICE": NotInVoiceError,
    "USER_OWNS_GUILDS": UserOwnsGuildsError,
    "VALIDATION_ERROR": ValidationError,
    "VOICE_CHANNEL_FULL": VoiceChannelFullError,
    "WEBAUTHN_CREDENTIAL_LIMIT_REACHED": WebAuthnCredentialLimitReachedError,
}


# ---------------------------------------------------------------------------
# Response error helper
# ---------------------------------------------------------------------------

def try_raise_error(raw_json: dict[str, Any], status_code: int) -> dict[str, Any]:
    """Check for errors in the API response and raise appropriate exceptions.

    Parameters
    ----------
    raw_json:
        The JSON response from the API.
    status_code:
        The HTTP status code.

    Returns
    -------
    dict
        *raw_json* unchanged, if no error was detected.

    Raises
    ------
    FluxCrystalError
        The most specific subclass that matches the response.
    """
    if status_code in (200, 201, 204):
        return raw_json

    # Prefer the API error code for the most specific exception.
    error_code: str | None = raw_json.get("code")
    if error_code and error_code in ERROR_CODE_MAPPING:
        error_cls = ERROR_CODE_MAPPING[error_code]
        message: str = raw_json.get("message", f"Error code: {error_code}")
        if error_cls is RateLimitedError:
            retry_after: float = float(raw_json.get("retry_after", 0))
            raise RateLimitedError(message, retry_after=retry_after)
        raise error_cls(message)

    # Fall back to HTTP status.
    http_message: str = raw_json.get("message", "")
    if status_code == 400:
        raise BadRequestError(http_message or "Bad request")
    if status_code == 401:
        raise UnauthorizedError(http_message or "Unauthorized")
    if status_code == 403:
        raise ForbiddenError(http_message or "Forbidden")
    if status_code == 404:
        raise NotFoundError(http_message or "Not found")
    if status_code == 405:
        raise MethodNotAllowedError(http_message or "Method not allowed")
    if status_code == 429:
        retry_after = float(raw_json.get("retry_after", 0))
        raise RateLimitedError(http_message or "Rate limited", retry_after=retry_after)
    if status_code == 502:
        raise BadGatewayError(http_message or "Bad gateway")
    if status_code == 503:
        raise ServiceUnavailableError(http_message or "Service unavailable")

    return raw_json
