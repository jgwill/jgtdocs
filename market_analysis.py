#!/usr/bin/env python3
"""
Market Data Analysis for Trading Opportunities
Analyzes SPX500, EUR/USD, AUD/USD, USD/CAD on H4 and D1 timeframes
"""

import pandas as pd
import numpy as np
from pathlib import Path

def load_market_data(instrument, timeframe):
    """Load market data from PDS files"""
    file_path = Path(f"data/current/pds/{instrument}_{timeframe}.csv")
    if not file_path.exists():
        return None
    
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df

def calculate_levels(df, lookback=20):
    """Calculate support/resistance levels and basic indicators"""
    if df is None or len(df) < lookback:
        return None
    
    # Take recent data
    recent = df.tail(lookback).copy()
    
    # Basic calculations
    recent['SMA_20'] = recent['Close'].rolling(window=min(20, len(recent))).mean()
    recent['High_Max'] = recent['High'].rolling(window=min(10, len(recent))).max()
    recent['Low_Min'] = recent['Low'].rolling(window=min(10, len(recent))).min()
    
    # Current price info
    current = recent.iloc[-1]
    previous = recent.iloc[-2] if len(recent) > 1 else current
    
    # Support/Resistance
    resistance = recent['High_Max'].iloc[-1]
    support = recent['Low_Min'].iloc[-1]
    
    # Trend direction (simple)
    trend = "UP" if current['Close'] > current['SMA_20'] else "DOWN"
    
    # Price action
    price_change = current['Close'] - previous['Close']
    price_change_pct = (price_change / previous['Close']) * 100
    
    return {
        'current_price': current['Close'],
        'previous_close': previous['Close'],
        'price_change': price_change,
        'price_change_pct': price_change_pct,
        'resistance': resistance,
        'support': support,
        'sma_20': current['SMA_20'],
        'trend': trend,
        'date': current['Date'],
        'volume': current.get('Volume', 0)
    }

def analyze_opportunity(levels_d1, levels_h4, instrument):
    """Analyze trading opportunities based on multi-timeframe analysis"""
    if not levels_d1 or not levels_h4:
        return None
    
    opportunities = []
    
    # Multi-timeframe trend alignment
    trend_aligned = levels_d1['trend'] == levels_h4['trend']
    
    # Price near support/resistance
    d1_price = levels_d1['current_price']
    d1_support = levels_d1['support']
    d1_resistance = levels_d1['resistance']
    
    support_distance = abs(d1_price - d1_support) / d1_price * 100
    resistance_distance = abs(d1_price - d1_resistance) / d1_price * 100
    
    # Opportunity detection
    if trend_aligned and levels_d1['trend'] == "UP":
        if support_distance < 1.0:  # Within 1% of support
            opportunities.append({
                'type': 'BUY',
                'reason': 'Uptrend + Price near support',
                'confidence': 'HIGH' if support_distance < 0.5 else 'MEDIUM',
                'entry_level': d1_support,
                'stop_loss': d1_support * 0.995,  # 0.5% below support
                'target': d1_resistance
            })
    
    elif trend_aligned and levels_d1['trend'] == "DOWN":
        if resistance_distance < 1.0:  # Within 1% of resistance
            opportunities.append({
                'type': 'SELL',
                'reason': 'Downtrend + Price near resistance',
                'confidence': 'HIGH' if resistance_distance < 0.5 else 'MEDIUM',
                'entry_level': d1_resistance,
                'stop_loss': d1_resistance * 1.005,  # 0.5% above resistance
                'target': d1_support
            })
    
    return {
        'instrument': instrument,
        'current_price': d1_price,
        'd1_trend': levels_d1['trend'],
        'h4_trend': levels_h4['trend'],
        'trend_aligned': trend_aligned,
        'support': d1_support,
        'resistance': d1_resistance,
        'opportunities': opportunities,
        'd1_change_pct': levels_d1['price_change_pct'],
        'h4_change_pct': levels_h4['price_change_pct']
    }

def main():
    """Main analysis function"""
    instruments = ['SPX500', 'EUR-USD', 'AUD-USD', 'USD-CAD']
    timeframes = ['D1', 'H4']
    
    print("=" * 80)
    print("JGT PLATFORM - MARKET ANALYSIS FOR TRADING OPPORTUNITIES")
    print("=" * 80)
    print(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    all_analyses = []
    
    for instrument in instruments:
        print(f"\n📊 ANALYZING {instrument}")
        print("-" * 50)
        
        # Load data for both timeframes
        levels_d1 = None
        levels_h4 = None
        
        for tf in timeframes:
            df = load_market_data(instrument, tf)
            levels = calculate_levels(df)
            
            if levels:
                if tf == 'D1':
                    levels_d1 = levels
                else:
                    levels_h4 = levels
                
                print(f"{tf}: {levels['current_price']:.5f} ({levels['price_change_pct']:+.2f}%) "
                      f"Trend: {levels['trend']} | S: {levels['support']:.5f} | R: {levels['resistance']:.5f}")
        
        # Analyze opportunities
        analysis = analyze_opportunity(levels_d1, levels_h4, instrument)
        if analysis:
            all_analyses.append(analysis)
            
            print(f"Trend Alignment: {'✅' if analysis['trend_aligned'] else '❌'}")
            
            if analysis['opportunities']:
                for opp in analysis['opportunities']:
                    print(f"🎯 {opp['type']} OPPORTUNITY ({opp['confidence']})")
                    print(f"   Reason: {opp['reason']}")
                    print(f"   Entry: {opp['entry_level']:.5f}")
                    print(f"   Stop: {opp['stop_loss']:.5f}")
                    print(f"   Target: {opp['target']:.5f}")
            else:
                print("🔍 No clear opportunities at current levels")
    
    # Summary
    print("\n" + "=" * 80)
    print("📋 TRADING OPPORTUNITIES SUMMARY")
    print("=" * 80)
    
    total_opps = sum(len(a['opportunities']) for a in all_analyses)
    if total_opps > 0:
        print(f"Found {total_opps} trading opportunities:")
        for analysis in all_analyses:
            for opp in analysis['opportunities']:
                risk_reward = abs((opp['target'] - opp['entry_level']) / (opp['stop_loss'] - opp['entry_level']))
                print(f"• {analysis['instrument']}: {opp['type']} @ {opp['entry_level']:.5f} "
                      f"(R:R {risk_reward:.1f}:1, {opp['confidence']})")
    else:
        print("No clear trading opportunities identified at current market levels.")
        print("Consider waiting for better setups or price action confirmation.")
    
    print(f"\n💡 Analysis completed using available data up to June 17, 2025")
    print(f"📈 For live trading, ensure data refresh and signal confirmation")

if __name__ == "__main__":
    main() 