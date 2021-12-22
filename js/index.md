# JavaScript

## TIPS

### Zero Padding

```javascript
/**
 * zeroPadding(123, 5) -> '00123'
 */
function zeroPadding (value, digit) {
  return ('0'.repeat(digit) + value).slice(-digit);
}
```
